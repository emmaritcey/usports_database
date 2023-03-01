
'''
Script runs all of the data scraping and cleaning
'''

import preprocessUtils.scrape_player_data as scrape_player_data, preprocessUtils.scrape_team_data as scrape_team_data
import preprocessUtils.clean_data as clean_data
import os


def main():
    
    scrape = 0
    clean = 1
    ind_plyr_avgs = 1
    plyr_stat_types = ['general', 'ball control', 'shooting']
    team_avgs = 0
    team_stat_type = ['splitstat']
    
    wdir = os.getcwd()
    data_save_path = wdir + "/raw_csv_files/"
    
    if scrape and ind_plyr_avgs:
        scrape_player_data.run_scraping(plyr_stat_types, data_save_path)
        
    if scrape and team_avgs:    
        scrape_team_data.run_scraping(team_stat_type, data_save_path)
            
    if clean and ind_plyr_avgs:
        
        #the tables that are being created
        data = ['players', 'player_info', 'player_shooting', 'player_ballcntrl', 'teams']

        clean_data.create_tables(data, wdir)

main()