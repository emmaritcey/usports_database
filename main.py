import os
from src.scrape_data import run_scraping


if __name__ == "__main__":
    wdir = os.getcwd()
    print(wdir)
    run_scraping()