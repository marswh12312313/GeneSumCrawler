from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import re
import csv


# 爬虫的主要功能
def scrape_gene_summaries(gene):
    # 在函数内部创建新的WebDriver服务
    webdriver_service = Service('geckodriver')  # 替换为你的GeckoDriver路径
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')  # 无头模式
    driver = webdriver.Firefox(service=webdriver_service, options=options)

    try:
        url = f"https://www.genecards.org/cgi-bin/carddisp.pl?gene={gene}"
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "summaries")))
        page_source = driver.page_source
    except Exception as e:
        print(f"Failed to load summaries for {gene}: {e}")
        driver.quit()
        return []

    soup = BeautifulSoup(page_source, 'html.parser')
    driver.quit()  # 关闭浏览器实例

    summaries = []
    summaries_section = soup.find('section', id='summaries')
    if summaries_section:
        ncbi_pattern = re.compile(f'NCBI Gene Summary for {gene} Gene')
        genecards_pattern = re.compile(f'GeneCards Summary for {gene} Gene')
        uniprot_pattern = re.compile(f'UniProtKB/Swiss-Prot Summary for {gene} Gene')

        ncbi_summary = summaries_section.find('h3', string=ncbi_pattern)
        if ncbi_summary:
            ncbi_summary_text = ncbi_summary.find_next('p').text
            summaries.append((gene, 'NCBI Gene Summary', ncbi_summary_text))

        genecards_summary = summaries_section.find('h3', string=genecards_pattern)
        if genecards_summary:
            genecards_summary_text = genecards_summary.find_next('p').text
            summaries.append((gene, 'GeneCards Summary', genecards_summary_text))

        uniprot_summary = summaries_section.find('h3', string=uniprot_pattern)
        if uniprot_summary:
            uniprot_summary_text = uniprot_summary.find_next('p').text
            summaries.append((gene, 'UniProtKB/Swiss-Prot Summary', uniprot_summary_text))

    return summaries


def main():
    gene_list = pd.read_csv('genelist.csv').iloc[:, 0].tolist()
    total_genes = len(gene_list)

    with open('gene_summaries.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Gene', 'Summary Type', 'Summary'])

    for index, gene in enumerate(gene_list, start=1):
        gene_data = scrape_gene_summaries(gene)
        if gene_data:
            with open('gene_summaries.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(gene_data)
            print(f"Progress: {index}/{total_genes} genes processed. Gene '{gene}' summaries fetched.")
        else:
            print(f"Progress: {index}/{total_genes} genes processed. No summaries found for gene '{gene}'.")

    print("Data scraping complete. Data saved to gene_summaries.csv.")


if __name__ == "__main__":
    main()
    