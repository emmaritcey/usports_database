'''
scrape individual player data from USports women's basketball website
scrape each data type individually to separate csv files (shooting, ball control, or general)
YEARS: indicates years to scrape data from
'''

import requests
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen as uReq
from preprocessUtils.scraping_helpers import parse_values_player, parse_shooting, parse_name

TEAMS =  ['acadia', 'capebreton', 'dalhousie', 'memorial', "saintmarys", 'stfx', 'unb', 'upei',
        'bishops', 'concordia', 'laval', 'mcgill', 'uqam', 'algoma', 'brock', 'carleton', 
        'guelph', 'lakehead', 'laurentian', 'laurier', 'mcmaster', 'nipissing', 'ontariotech', 
        'ottawa', 'queens', 'ryerson', 'toronto', 'torontometropolitan', 'waterloo', 'western', 'windsor', 
        'york', 'alberta', 'brandon', 'calgary', 'lethbridge', 'macewan', 'manitoba', 'mountroyal', 
        'regina', 'saskatchewan', 'thompsonrivers', 'trinitywestern', 'ubc', 'ubcokanagan',
        'ufv', 'unbc', 'victoria', 'winnipeg']
TEAMS = ['acadia']

YEARS = ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2021-22', '2022-23']
YEARS = ['2022-23']


def get_player_stats(stat_type, headers, table_index, fileName):

    base_url = 'https://universitysport.prestosports.com/sports/wbkb/'
    end_url = '?view=lineup&r=0&pos=sh'

    rows = [headers]

    for year in YEARS:
        for team in TEAMS:
            current_url = base_url + year + '/teams/' + team + end_url
            print(current_url)
            r = requests.get(current_url) #extract the HTML code from current url
            raw_html = r.content #get just the content from HTML code
            #print(raw_html)
            soup = BeautifulSoup(raw_html, 'html.parser') #create parser called soup that uses contents of raw_html
            tables = soup.findAll('table') #tables contains all table elements from current page
            
            if len(tables) > 0: #check that this team has data or current year
                index = table_index #specifies which table/stats to collect
                players_tbl = tables[index]
                players = players_tbl.findAll('tr') #get all url's in table 
        
                #loop through each player (each row of the table)
                for player in players[1:len(players)-2]:
                    #print(player)
                    stats = player.find_all("td") #extract text from every column item/table data

                    if stat_type == 'general':
                        number = stats[0].text

                        #get name
                        name = parse_name(stats[1].text) #name is long string with spaces and new line characters
                    
                        team_name = team
                        season_year = int(year[0:2]+year[-2:]) #year is by year that Natty Championship is held
                        player_year = parse_values_player(stats[2].text)
                        
                        gp = float(parse_values_player(stats[4].text))
                        gs = float(parse_values_player(stats[5].text))
                        min_pg = float(parse_values_player(stats[6].text))
                        
                        rows.append([name, team_name, season_year, player_year, number, gp, gs, min_pg])
                        
                    elif stat_type == 'shooting':
                        name = parse_name(stats[1].text) #name is long string with spaces and new line characters
                        season_year = int(year[0:2]+year[-2:]) #year is by year that Natty Championship is held

                        fgm, fga = parse_shooting(parse_values_player(stats[7].text))
                        fg_pct = float(parse_values_player(stats[8].text))
                        fgm3, fga3 = parse_shooting(parse_values_player(stats[9].text))
                        fg3_pct = float(parse_values_player(stats[10].text))
                        ftm, fta = parse_shooting(parse_values_player(stats[11].text))
                        ft_pct = float(parse_values_player(stats[12].text))
                        ppg = float(parse_values_player(stats[13].text))
        
                        rows.append([name, season_year, fgm, fga, fg_pct, fgm3, fga3, fg3_pct, ftm, fta, ft_pct, ppg])
                        
                    elif stat_type == 'ball control':
                        name = parse_name(stats[1].text) #name is long string with spaces and new line characters
                        season_year = int(year[0:2]+year[-2:]) #year is by year that Natty Championship is held
                        
                        reb_def = float(parse_values_player(stats[7].text))
                        reb_off = float(parse_values_player(stats[8].text))
                        reb = float(parse_values_player(stats[9].text))
                        pf = float(parse_values_player(stats[10].text))
                        apg = float(parse_values_player(stats[12].text))
                        to = float(parse_values_player(stats[13].text))
                        a_to_ratio = float(parse_values_player(stats[14].text))
                        stl = float(parse_values_player(stats[15].text))
                        blk = float(parse_values_player(stats[16].text))
                        
                        rows.append([name, season_year, reb_def, reb_off, reb, pf, apg, to, a_to_ratio, stl, blk])

    #write each row of table 'rows' to row in csv file
    with open(fileName,'w') as myfile:
       wrtr = csv.writer(myfile, delimiter=',')
       for row in rows:
           wrtr.writerow(row)
           myfile.flush() # whenever you want


def run_scraping(stat_type, data_save_path):
    for stat in stat_type:
        if stat == 'general':
            headers = ['NAME', 'TEAM', 'SEASON', 'PLYR_YR', 'NUM', 'GP', 'GS', 'MIN/G']
            table_index = 3
            fileName = data_save_path + 'player_stats_info.csv'
            fileName = data_save_path + 'info_test.csv'
            print("getting player info  stats...")
            get_player_stats(stat, headers, table_index, fileName)
        elif stat == 'shooting':
            headers = ['NAME', 'SEASON', 'FGM', 'FGA', 'FG%', '3FGM', '3FGA','3FG%', 'FTM', 'FTA', 'FT%', 'PPG']
            table_index = 3
            fileName = data_save_path + 'player_stats_shooting.csv'
            fileName = data_save_path + 'sh_test.csv'
            print("getting player shooting stats...")
            get_player_stats(stat, headers, table_index, fileName)
        elif stat == 'ball control':
            headers = ['NAME', 'SEASON', 'DREB/G', 'OREB/G', 'REB/G', 'PF/G', 'A/G','TO/G', 'A/TO', 'STL/G', 'BLK/G']
            table_index = 4
            fileName = data_save_path + 'player_stats_ball_control.csv'
            fileName = data_save_path + 'bc_test.csv'
            print("getting player ball control stats...")
            get_player_stats(stat, headers, table_index, fileName)
        