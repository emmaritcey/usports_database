This repository contains code to scrape data from USports women's basketball website, save raw data into csv files, and clean data into new csv files

To install required libraries, run: pip install -r requirements.txt

To scrape individual player data run: scrape_player_data.py
    - global variables: 
        STAT_TYPE: determines which player data to collect, options are 'general info', 'shooting stats', 'ball control stats'
        TEAMS: list of teams to collect player data from 
        YEARS: years/seasons to collect player data from
    - saves raw data into csv files
    - general info data: missing values in 'NUM' and 'PLYR_YR' columns set to np.nan, missing data ('-') of numeric column set to 0

To create tables for each type of player data run: create_player_tables.py
    - uses raw data files to create tables
    - assigns each player a unique player_id that's consistent across all tables