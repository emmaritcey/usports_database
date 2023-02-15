'''
scrape individual player data from USports women's basketball website
scrape each data type individually to separate csv files (shooting, ball control, or general)
YEARS: indicates years to scrape data from
'''


import re
import requests
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen as uReq
import pandas as pd
import numpy as np

STAT_TYPE = 'general' #either 'shooting', 'ball control', or 'general'
TEAMS =  ['acadia', 'capebreton', 'dalhousie', 'memorial', "saintmarys", 'stfx', 'unb', 'upei',
        'bishops', 'concordia', 'laval', 'mcgill', 'uqam', 'algoma', 'brock', 'carleton', 
        'guelph', 'lakehead', 'laurentian', 'laurier', 'mcmaster', 'nipissing', 'ontariotech', 
        'ottawa', 'queens', 'toronto', 'torontometropolitan', 'waterloo', 'western', 'windsor', 
        'york', 'alberta', 'brandon', 'calgary', 'lethbridge', 'macewan', 'manitoba', 'mountroyal', 
        'regina', 'saskatchewan', 'thompsonrivers', 'trinitywestern', 'ubc', 'ubcokanagan',
        'ufv', 'unbc', 'victoria', 'winnipeg']

YEARS = ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2021-22']

def parse_name(string):
    temp_list = string.split(' ') #split into list, each ' ' is separate entry
    name = ''
    fn_flag = 0
    for idx in range(len(temp_list)): #loop through list, select first and last name, remove \n chars, 
        if len(temp_list[idx]) > 0 and temp_list[idx]!='\n\n' and temp_list[idx] != '\n':
            #check for upper limit as there are some text errors which cause super long strings (only a few cases)
            if len(temp_list[idx]) > 50:  #just use first three letters of first name
                end_idx = 4
            else:
                end_idx = -1
                  
            if fn_flag:
                name = name + ' ' + temp_list[idx][0:end_idx] #add space bw first and last, remove \n from end of text
            else:
                name = temp_list[idx][0:end_idx] #remove \n from end of text
                fn_flag = 1
    return name


def parse_values(string):
    temp_list = string.split(' ') #split into list, each ' ' is separate entry
    for idx in range(len(temp_list)): #loop through list, select first and last name, remove \n chars
        if len(temp_list[idx]) > 0 and temp_list[idx] != '\n':
            value = temp_list[idx][0:-1] #remove \n from end of text
    try:
        if value == '-':
            value = 0
    except:
        value = np.nan
        
        
    return value


def parse_shooting(fraction_str):
    makes_atts = fraction_str.split('-')
    makes = float(makes_atts[0])
    attempts = float(makes_atts[1])
    return makes, attempts


def get_player_stats(headers, table_index, fileName):
    print("getting player stats...")

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
                for player in players[1:len(players)-3]:
                    #print(player)
                    stats = player.find_all("td") #extract text from every column item/table data

                    if STAT_TYPE == 'general':
                        number = stats[0].text

                        #get name
                        name = parse_name(stats[1].text) #name is long string with spaces and new line characters
                    
                        team_name = team
                        season_year = int(year[0:2]+year[-2:]) #year is by year that Natty Championship is held
                        player_year = parse_values(stats[2].text)
                        
                        gp = float(parse_values(stats[4].text))
                        gs = float(parse_values(stats[5].text))
                        min_pg = float(parse_values(stats[6].text))
                        
                        rows.append([name, team_name, season_year, player_year, number, gp, gs, min_pg])
                        
                    elif STAT_TYPE == 'shooting':
                        name = parse_name(stats[1].text) #name is long string with spaces and new line characters
                        season_year = int(year[0:2]+year[-2:]) #year is by year that Natty Championship is held

                        fgm, fga = parse_shooting(parse_values(stats[7].text))
                        fg_pct = float(parse_values(stats[8].text))
                        fgm3, fga3 = parse_shooting(parse_values(stats[9].text))
                        fg3_pct = float(parse_values(stats[10].text))
                        ftm, fta = parse_shooting(parse_values(stats[11].text))
                        ft_pct = float(parse_values(stats[12].text))
                        ppg = float(parse_values(stats[13].text))
        
                        rows.append([name, season_year, fgm, fga, fg_pct, fgm3, fga3, fg3_pct, ftm, fta, ft_pct, ppg])
                        
                    elif STAT_TYPE == 'ball control':
                        name = parse_name(stats[1].text) #name is long string with spaces and new line characters
                        season_year = int(year[0:2]+year[-2:]) #year is by year that Natty Championship is held
                        
                        reb_def = float(parse_values(stats[7].text))
                        reb_off = float(parse_values(stats[8].text))
                        reb = float(parse_values(stats[9].text))
                        pf = float(parse_values(stats[10].text))
                        apg = float(parse_values(stats[12].text))
                        to = float(parse_values(stats[13].text))
                        a_to_ratio = float(parse_values(stats[14].text))
                        stl = float(parse_values(stats[15].text))
                        blk = float(parse_values(stats[16].text))
                        
                        rows.append([name, season_year, reb_def, reb_off, reb, pf, apg, to, a_to_ratio, stl, blk])

    #write each row of table 'rows' to row in csv file
    with open(fileName,'w') as myfile:
       wrtr = csv.writer(myfile, delimiter=',')
       for row in rows:
           wrtr.writerow(row)
           myfile.flush() # whenever you want


def main():
    
    if STAT_TYPE == 'general':
        headers = ['NAME', 'TEAM', 'SEASON', 'PLYR_YR', 'NUM', 'GP', 'GS', 'MIN/G']
        table_index = 3
        fileName = 'raw_csv_files/player_stats_info.csv'
        get_player_stats(headers, table_index, fileName)
    elif STAT_TYPE == 'shooting':
        headers = ['NAME', 'SEASON', 'FGM', 'FGA', 'FG%', '3FGM', '3FGA','3FG%', 'FTM', 'FTA', 'FT%', 'PPG']
        table_index = 3
        fileName = 'raw_csv_files/player_stats_shooting.csv'
        get_player_stats(headers, table_index, fileName)
    elif STAT_TYPE == 'ball control':
        headers = ['NAME', 'SEASON', 'DREB/G', 'OREB/G', 'REB/G', 'PF/G', 'A/G','TO/G', 'A/TO', 'STL/G', 'BLK/G']
        table_index = 4
        fileName = 'raw_csv_files/player_stats_ball_control.csv'
        get_player_stats(headers, table_index, fileName)
        
main()
