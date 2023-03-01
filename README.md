## USports Women's Basketball Data
This repository contains code to analyze and visualize USports women's basketball data.
Code includes scraping data from USports women's basketball website, saving raw data into csv files, cleaning data into new csv files, creating a relational database

## Requirements
To install required libraries, run: ***pip install -r requirements.txt***

## Data Scraping and Cleaning
To scrape individual player data run: ***collect_data.py ***
* saves data into csv files
* general info data: missing values in 'NUM' and 'PLYR_YR' columns set to np.nan, missing data ('-') of numeric column set to 0
* variables at beginning of main function determine what data to scrape/clean
* calls any of ***scrape_player_data.py, scrape_team_data.py, and/or clean_data.py***
* ***clean_data.py*** cleans the raw data produced from scraping

## SQL Database Creation
To create a relational database of the data, run: ***create_usports_database.py***
* uses functions in ***sql_functions.py ***
* takes the data from the csv files in tables folder (created with create_player_tables.py)
* Folder titled 'sql_code' contains .sql files created prior to moving over to python (not up to date)


    