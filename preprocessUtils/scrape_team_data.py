import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import csv

from preprocessUtils.scraping_helpers import parse_shooting, parse_values_team


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

def get_team_splitstats(headers, fileName):
    print("getting links...")

    base_url = 'https://universitysport.prestosports.com/sports/wbkb/'
    end_url = '?view=splits'
    
    rows = [headers]
                 
    for year in YEARS:
        season = '20' + year[5:7]
        for team in TEAMS:
            current_url = base_url + year + '/teams/' + team + end_url
            print(current_url)
            r = requests.get(current_url) #extract the HTML code from current url
            raw_html = r.content #get just the content from HTML code
            soup = BeautifulSoup(raw_html, 'html.parser') #create parser called soup that uses contents of raw_html
            tables = soup.findAll('table') #tables contains all table elements from current page
            
            
            if len(tables) > 0: #check that this team has data or current year
                #some split stat tables are in different locations, find it by finding table with no url links
                for i in range(len(tables)):
                    tags = tables[i].findAll('a')
                    if len(tags) == 0:
                        table_index = i #specifies which table/stats to collect                   
                        splitstats_tbl = tables[table_index]
                        all_stats = splitstats_tbl.findAll('tr') #get all url's in table 
                    
                idx = 1
                for row in all_stats[1:len(all_stats)]:
                    if idx not in [3,6,7,10]: #skip empty rows
                        #print(row)
                        stats = row.find_all("td") #extract text from every column item/table data

                        #extract data from each column
                        category = stats[0].text #split stat category
                        gp = float(parse_values_team(stats[1].text))
                        fgm, fga = parse_shooting(parse_values_team(stats[2].text))    
                        fg_pct = float(parse_values_team(stats[3].text))
                        fgm3, fga3 = parse_shooting(parse_values_team(stats[4].text))
                        fg3_pct = float(parse_values_team(stats[5].text))
                        ftm, fta = parse_shooting(parse_values_team(stats[6].text))
                        ft_pct = float(parse_values_team(stats[7].text))
                        reb_def = float(parse_values_team(stats[8].text))
                        reb_off = float(parse_values_team(stats[9].text))
                        reb = float(parse_values_team(stats[10].text))
                        apg = float(parse_values_team(stats[11].text))
                        to = float(parse_values_team(stats[12].text))
                        stl = float(parse_values_team(stats[13].text))
                        blk = float(parse_values_team(stats[14].text))
                        pf = float(parse_values_team(stats[15].text))
                        ppg = float(parse_values_team(stats[16].text))
                        off_eff = float(parse_values_team(stats[17].text))
                        net_eff = float(parse_values_team(stats[18].text))
                        
                        rows.append([season, team, category, gp, fgm, fga, fg_pct, fgm3, fga3, fg3_pct, ftm, fta, ft_pct,
                                    reb_def, reb_off, reb, apg, to, stl, blk, pf, ppg, off_eff, net_eff])
                    idx += 1
                
    #write each row of table 'rows' to row in csv file
    with open(fileName,'w') as myfile:
        wrtr = csv.writer(myfile, delimiter=',')
        for row in rows:
            wrtr.writerow(row)
            myfile.flush()                
    

def run_scraping(stat_type, data_save_path):
    for stat in stat_type:
        if stat == 'splitstat':
            headers = ['SEASON', 'TEAM', 'SPLIT', 'GP', 'FGM', 'FGA', 'FG%', '3FGM', '3FGA','3FG%', 'FTM', 'FTA', 'FT%', 
                        'DREB/G', 'OREB/G', 'REB/G', 'A/G','TO/G', 'STL/G', 'BLK/G','PF/G', 'PPG', 'OFF_EFF', 'NET_EFF']
            fileName = data_save_path + 'team_splitstats.csv'
            fileName = data_save_path + 'test.csv'
            get_team_splitstats(headers, fileName)