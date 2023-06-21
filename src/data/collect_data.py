
'''
Script runs all of the data scraping, cleaning, and creating of SQL database
'''

import preprocessUtils.scrape_player_data as scrape_player_data, preprocessUtils.scrape_team_data as scrape_team_data
import preprocessUtils.clean_data as clean_data
import preprocessUtils.update_names as update_names
import preprocessUtils.fix_duplicate_names as fix_duplicate_names
import os


def main():
    scrape = 0 #boolean to scrape data from website and save raw data as csv files
    clean = 1 #boolean to clean raw data and save as new csv files
    ind_plyr_avgs = 1 #boolean to run scraping/cleaning on individual player data
    plyr_stat_types = ['general', 'ball control', 'shooting'] #three types of player data to collect
    team_avgs = 0 #boolean to run scraping on team data
    team_stat_type = ['splitstat'] 
    
    wdir = os.getcwd()
    print(wdir)

    data_raw_path = wdir + "/data/raw/"
    
    if scrape and ind_plyr_avgs:
        scrape_player_data.run_scraping(plyr_stat_types, data_raw_path)
        
    if scrape and team_avgs:    
        scrape_team_data.run_scraping(team_stat_type, data_raw_path)
            
    if clean and ind_plyr_avgs:
        
        #the tables that are being created
        data = ['players', 'player_info', 'player_shooting', 'player_ballcntrl', 'teams']

        fix_duplicate_names.run()
        clean_data.create_tables(data, wdir)
        update_names.run()
        
        

main()

#TODO: scrape player split stats and add to database