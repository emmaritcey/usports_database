from pathlib import Path

#teams and years to run scraping on
TEAMS =  ['acadia', 'capebreton', 'dalhousie', 'memorial', "saintmarys", 'stfx', 'unb', 'upei',
        'bishops', 'concordia', 'laval', 'mcgill', 'uqam', 'algoma', 'brock', 'carleton', 
        'guelph', 'lakehead', 'laurentian', 'laurier', 'mcmaster', 'nipissing', 'ontariotech', 
        'ottawa', 'queens', 'ryerson', 'toronto', 'torontometropolitan', 'waterloo', 'western', 'windsor', 
        'york', 'alberta', 'brandon', 'calgary', 'lethbridge', 'macewan', 'manitoba', 'mountroyal', 
        'regina', 'saskatchewan', 'thompsonrivers', 'trinitywestern', 'ubc', 'ubcokanagan',
        'ufv', 'unbc', 'victoria', 'winnipeg']

YEARS = ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2021-22', '2022-23', '2023-24']
#YEARS = ['2022-23']


#Variables to define the specific data to scrape
SCRAPE = 1 #boolean to scrape data from website and save raw data as csv files
CLEAN = 1 #boolean to clean raw data and save as new csv files
IND_PLYR_AVGS = 0 #boolean to run scraping/cleaning on individual player data
PLYR_STAT_TYPES = ['info', 'stats'] #three types of player data to collect
TEAM_AVGS = 1 #boolean to run scraping on team data
TEAM_STAT_TYPE = ['splitstat'] 

RAW_DATA_PATH = Path(__file__).parent.parent / "data" / "raw" 