'''
scrape individual player data from USports women's basketball website
scrape each data type individually to separate csv files (shooting, ball control, or general)
YEARS: indicates years to scrape data from
'''

import requests
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen as uReq
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

from src.scrapingUtils.scraping_helpers import scrape_table_rows, parse_values_player, parse_shooting, parse_name
from src.settings import TEAMS, YEARS

# TEAMS =  ['acadia', 'capebreton', 'dalhousie', 'memorial', "saintmarys", 'stfx', 'unb', 'upei',
#         'bishops', 'concordia', 'laval', 'mcgill', 'uqam', 'algoma', 'brock', 'carleton', 
#         'guelph', 'lakehead', 'laurentian', 'laurier', 'mcmaster', 'nipissing', 'ontariotech', 
#         'ottawa', 'queens', 'ryerson', 'toronto', 'torontometropolitan', 'waterloo', 'western', 'windsor', 
#         'york', 'alberta', 'brandon', 'calgary', 'lethbridge', 'macewan', 'manitoba', 'mountroyal', 
#         'regina', 'saskatchewan', 'thompsonrivers', 'trinitywestern', 'ubc', 'ubcokanagan',
#         'ufv', 'unbc', 'victoria', 'winnipeg']

# YEARS = ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2021-22', '2022-23']

def get_player_stats(fileName):

    base_url = 'https://universitysport.prestosports.com/sports/wbkb/'
    end_url = '?view=lineup'

    info_rows = [['Num', 'Name', 'Yr', 'Pos',]]
    stats_rows = [['GP', 'GS', 'Min', 'FG', 'Pct', '3FG', '3Pct', 'FT', 'FTPct', 'Pts', 'OReb', 'DReb', 'Reb', 'Ast', 'TO', 'Stl', 'Blk']]
    flag_MR = 0
    flag_ET = 0
    flag_EJ = 0
    
    df_stats_all = pd.DataFrame(columns = ['Num', 'Name', 'Yr', 'Pos', 'GP', 'GS', 'Min', 'Pct', '3Pct', 'FTPct',
       'Pts', 'FGM', 'FGA', '3FGM', '3FGA', 'FTM', 'FTA', 'OReb', 'DReb',
       'Reb', 'Ast', 'TO', 'Stl', 'Blk', 'Team', 'Season'])

    for year in YEARS:
        season_year = int(year[0:2]+year[-2:]) #year is by year that Natty Championship is held
        for team in TEAMS:
            
            if (team == 'algoma' and season_year < 2014):
                continue
            if (team == 'ontariotech' and season_year < 2020):
                continue
            if (team == 'nipissing' and season_year < 2015):
                continue
            if (team == 'macewan' and season_year < 2015):
                continue
            if (team == 'mountroyal' and season_year < 2013):
                continue
            if (team == 'ubcokanagan' and season_year < 2012):
                continue
            if (team == 'unbc' and season_year < 2013):
                continue
            if (team == 'torontometropolitan' and season_year < 2023):
                continue
            if (team == 'ryerson' and season_year > 2022):
                continue
            
            
            offensive_url = base_url + year + '/teams/' + team + end_url +'&pos=sh'
            
            # Provide the path to your ChromeDriver executable
            chromedriver_path = 'chromedriver-mac-x64/chromedriver' 
            service = Service(chromedriver_path)
            driver = webdriver.Chrome(service=service)
            driver.get(offensive_url)
            
            # table = WebDriverWait(driver, 10).until(
            #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".table.table-hover.table-light.nowrap.w-100.dataTable.dtfc-has-start.dtfc-has-left"))
            #     )
            
            # # Wait for the table to be visible
            table = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".table.table-hover.table-light.nowrap.w-100.dataTable.dtfc-has-start.dtfc-has-left"))
            )
            
            tab_pane = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.tab-pane.active#gamelog-lineup-sh"))
                )
            
            #find lineup table 
            #table = driver.find_element(By.CSS_SELECTOR, ".table.table-hover.table-light.nowrap.w-100.dataTable.dtfc-has-start.dtfc-has-left")
            #tbody = table.find_element(By.TAG_NAME, "tbody")
            tbody = tab_pane.find_element(By.CSS_SELECTOR, ".table.table-hover.table-light.nowrap.w-100.dataTable.dtfc-has-start.dtfc-has-left tbody")
            
            #extract rows from table
            rows = tbody.find_elements(By.TAG_NAME, "tr")
            
            off_columns = ['Num', 'Name', 'Yr', 'Pos', 'GP', 'GS', 'Min', 'FG', 'Pct', '3FG', '3Pct', 'FT', 'FTPct', 'Pts']  # 'OffReb', 'DefReb', 'Reb', ]
            scraped_df = scrape_table_rows(rows, off_columns)
                    
            scraped_df[['FGM', 'FGA']] = scraped_df['FG'].apply(lambda x: pd.Series(parse_shooting(x)))
            scraped_df[['3FGM', '3FGA']] = scraped_df['3FG'].apply(lambda x: pd.Series(parse_shooting(x)))
            scraped_df[['FTM', 'FTA']] = scraped_df['FT'].apply(lambda x: pd.Series(parse_shooting(x)))
            
            scraped_df.drop(['FG', '3FG', 'FT'], axis=1, inplace=True)
            print('DONE OFF STATS')
            #ballcontrol_url = base_url + year + '/teams/' + team + end_url + '&pos=bc'
            #driver.get(ballcontrol_url)
            
            ballcontrol_url = base_url + year + '/teams/' + team + end_url +'&pos=bc'
            driver.get(ballcontrol_url)
            
            
             # Wait for the table to be visible so that everything else loads
            table = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".table.table-hover.table-light.nowrap.w-100.dataTable.dtfc-has-start.dtfc-has-left"))
            )
            
            tab_pane_bc = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.tab-pane.active#gamelog-lineup-bc"))
                )

            tbody_bc = tab_pane_bc.find_element(By.CSS_SELECTOR, ".table.table-hover.table-light.nowrap.w-100.dataTable.dtfc-has-start.dtfc-has-left tbody")
            
            #extract rows from table
            rows_bc = tbody_bc.find_elements(By.TAG_NAME, "tr")
            
            bc_columns = ['Num', 'Name', 'Yr', 'Pos', 'GP', 'GS', 'OReb', 'DReb', 'Reb', 'Ast', 'TO', 'Stl', 'Blk']  # 'OffReb', 'DefReb', 'Reb', ]
            scraped_bc = scrape_table_rows(rows_bc, bc_columns)
            print('DONE BC STATS')
            
            driver.close()
            
            df_stats = pd.merge(scraped_df, scraped_bc, how='left', on=['Num', 'Name', 'Yr', 'Pos', 'GP', 'GS'])
            
            #add season and team to dataframe
            df_stats['Team'] = team
            df_stats['Season'] = season_year
            
            #fix name with tons of @@@@ chars
            if (season_year == 2022 and team == 'acadia'):
                df_stats.loc[df_stats['Name'].str.len() > 50, 'Name'] = 'Amelie Bouchard'

            #append current df to df with all players
            df_stats_all = pd.concat([df_stats_all, df_stats], ignore_index=True)
            
    #write each row of table 'rows' to row in csv file
    df_stats_all.to_csv(fileName + '/player_stats.csv', index=False)


# def run_player_scraping(stat_type, data_save_path):
#     for stat in stat_type:
#         if stat == 'general':
#             headers = ['NAME', 'TEAM', 'SEASON', 'PLYR_YR', 'NUM', 'GP', 'GS', 'MIN/G']
#             table_index = 3
#             fileName = data_save_path + 'player_stats_info.csv'
#             #fileName = data_save_path + 'info_test.csv'
#             print("getting player info  stats...")
#             get_player_stats(stat, headers, table_index, fileName)
#         elif stat == 'shooting':
#             headers = ['NAME', 'SEASON', 'FGM', 'FGA', 'FG%', '3FGM', '3FGA','3FG%', 'FTM', 'FTA', 'FT%', 'PPG']
#             table_index = 3
#             fileName = data_save_path + 'player_stats_shooting.csv'
#             #fileName = data_save_path + 'sh_test.csv'
#             print("getting player shooting stats...")
#             get_player_stats(stat, headers, table_index, fileName)
#         elif stat == 'ball control':
#             headers = ['NAME', 'SEASON', 'DREB/G', 'OREB/G', 'REB/G', 'PF/G', 'A/G','TO/G', 'A/TO', 'STL/G', 'BLK/G']
#             table_index = 4
#             fileName = data_save_path + 'player_stats_ball_control.csv'
#             #fileName = data_save_path + 'bc_test.csv'
#             print("getting player ball control stats...")
#             get_player_stats(stat, headers, table_index, fileName)
        