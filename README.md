# GeneCards Web Scraper

## Project Overview

This project contains a Python script for web scraping, designed to extract summary information about genes from the [GeneCards](https://www.genecards.org/) website. The script reads a list of genes from a CSV file, accesses each gene's page on GeneCards, extracts specific summary information, and saves this information to another CSV file.

## Features

- Extracts summary information for specified genes.
- Reads gene lists from a CSV file.
- Outputs results in a CSV file for easy analysis.

## How to Use

### Prerequisites

- Python 3.x
- [Selenium](https://www.selenium.dev/)
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas](https://pandas.pydata.org/)

### Installation Steps

1. Clone the repository to your local machine:

```
git clone [Your Repository Link]
```
2. Install the dependencies:
```
pip install selenium beautifulsoup4 pandas
```

3. Ensure [GeckoDriver](https://github.com/mozilla/geckodriver) is correctly installed on your system.

### Running the Script

1. Save your list of genes in a file named `genelist.csv`, with each gene name on a new line.

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
