## USports Women's Basketball Data
This repository contains code to analyze and visualize USports women's basketball data.\
Code includes scraping data from USports women's basketball website, saving raw data into csv files, cleaning data into new csv files, creating a relational database

## Requirements
To install required libraries, run: pip install -r requirements.txt

## Data Scraping
To scrape individual player data run: scrape_player_data.py \
&emsp - global variables: \
&emsp &emsp STAT_TYPE: determines which player data to collect, options are 'general info', 'shooting stats', 'ball control stats'\
&emsp &emsp TEAMS: list of teams to collect player data from \
&emsp &emsp YEARS: years/seasons to collect player data from \
&emsp - saves raw data into csv files\
&emsp - general info data: missing values in 'NUM' and 'PLYR_YR' columns set to np.nan, missing data ('-') of numeric column set to 0

## Data Cleaning
To create tables for each type of player data run: create_player_tables.py\
&emsp - uses raw data files to create tables\
&emsp - assigns each player a unique player_id that's consistent across all tables

## SQL Database Creation
To create a relational database of the data, run" create_usports_database.py\
&emsp - uses functions in sql_functions.py \
&emsp - takes the data from the csv files in tables folder (created with create_player_tables.py)
Folder titled 'sql_code' contains .sql files created prior to moving over to python (not up to date)


    