<p align="center">
  <img src="https://image.marswh.top/123-removebg-preview.png" width="200" height="200" />
</p>

<h1 align="center">GeneCards Web Scraper</h1>

<p align="center">
  <!-- Python Version -->
  <img src="https://img.shields.io/badge/python-3.10-blue.svg" alt="Python version" />
  
  <!-- License -->
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT" />

  <!-- GeneCards Link -->
  <a href="https://www.genecards.org/">
    <img src="https://img.shields.io/badge/Visit-GeneCards-orange.svg" alt="Visit GeneCards" />
  </a>
</p>

## Project Overview

This project contains a Python script for web scraping, designed to extract summary information about genes from the [GeneCards](https://www.genecards.org/) website. The script reads a list of genes from a CSV file, accesses each gene's page on GeneCards, extracts specific summary information, and saves this information to another CSV file.

## Features

- Extracts summary information for specified genes.
- Reads gene lists from a CSV file.
- Outputs results in a CSV file for easy analysis.

## How to Use

### Prerequisites

- Python 3.10
- [Selenium](https://www.selenium.dev/)
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas](https://pandas.pydata.org/)

### Installation Steps

1. Clone the repository to your local machine:

```
git clone https://github.com/marswh12312313/GeneSumCrawler.git
```
2. Install the dependencies:
```
pip install selenium beautifulsoup4 pandas
```


3. **GeckoDriver**:
- The repository includes a GeckoDriver binary suitable for Linux systems, located in the root directory.
- If you are using a different operating system (Windows or macOS), please download the appropriate version of GeckoDriver from [GeckoDriver Releases](https://github.com/mozilla/geckodriver/releases) and replace the existing file in the root directory, or update the script to point to your installed location of GeckoDriver.
- Ensure [GeckoDriver](https://github.com/mozilla/geckodriver) is correctly installed and in your system's PATH, or update the script with the correct path to the GeckoDriver executable.


### Running the Script

1. Save your list of genes in a file named `genelist.csv` in root directory, with each gene name on a new line.

2. Run the script:
```
python gene_spider.py
```

3. The results will be saved in a file named `gene_summaries.csv`.

## License

[MIT](LICENSE)

## Contributions

Contributions are welcome! Please submit pull requests or open issues to discuss proposed changes.

## Contact

You can request an issue.
