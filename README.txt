This repository contains code to scrape data from USports women's basketball website, save raw data into csv files, and clean data into new csv files

To install required libraries, run: pip install -r requirements.txt

To scrape individual player data run: scrape_player_data.py
    - global variables: 
        STAT_TYPE: determines which player data to collect, options are 'general info', 'shooting stats', 'ball control stats'
        TEAMS: list of teams to collect player data from 
        YEARS: years/seasons to collect player data from
    - saves raw data into csv files