
'''
Script runs all of the data scraping, cleaning, and creating of SQL database
'''
import os

import src.scrapingUtils.scrape_player_data as scrape_player_data
import src.scrapingUtils.scrape_team_data as scrape_team_data
# import src.scrapingUtils.clean_data as clean_data
# import src.scrapingUtils.update_names as update_names
# import src.scrapingUtils.fix_duplicate_names as fix_duplicate_names
from src.settings import RAW_DATA_PATH, SCRAPE, CLEAN, IND_PLYR_AVGS, PLYR_STAT_TYPES, TEAM_AVGS, TEAM_STAT_TYPE


def run_scraping():
    # scrape = 0 #boolean to scrape data from website and save raw data as csv files
    # clean = 1 #boolean to clean raw data and save as new csv files
    # ind_plyr_avgs = 1 #boolean to run scraping/cleaning on individual player data
    # plyr_stat_types = ['general', 'ball control', 'shooting'] #three types of player data to collect
    # team_avgs = 0 #boolean to run scraping on team data
    # team_stat_type = ['splitstat'] 
    print(RAW_DATA_PATH)
    # data_raw_path = wdir + "/data/raw/"
    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    
    if SCRAPE and IND_PLYR_AVGS:
        print('Scraping player data...')
        scrape_player_data.get_player_stats(str(RAW_DATA_PATH))
        
    if SCRAPE and TEAM_AVGS:    
        scrape_team_data.run_team_scraping(TEAM_STAT_TYPE, RAW_DATA_PATH)
            
    # if CLEAN and IND_PLYR_AVGS:
        
    #     #the tables that are being created
    #     data = ['players', 'player_info', 'player_shooting', 'player_ballcntrl', 'teams']

    #     fix_duplicate_names.run()
    #     clean_data.create_tables(data, wdir)
    #     update_names.run()
        

#TODO: scrape player split stats and add to database