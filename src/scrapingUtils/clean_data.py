import pandas as pd
import numpy as np
import os


'''
Create table with all players names and player id's
Table Columns: player_id, NAME
'''
def get_players_tbl(curr_path):
    #load names of all players from each season from raw csv
    player_names = pd.read_csv(curr_path + '/data/duplicates_removed/player_stats_info.csv', usecols=['NAME'])
    #remove duplicate names, only keep one row for each player
    players_tbl = player_names.drop_duplicates(ignore_index=True)

    #save to csv file where index is player id
    players_tbl.to_csv(curr_path + '/data/processed/players.csv', index_label='player_id')
    #players_tbl.to_csv(curr_path + '/data/tables/players_test.csv', index_label='player_id')


'''
Create table containing stats for all players
player_id obtained from table in players.csv  and matched based on player name   
INPUT:
    - curr_path: current path
    - columns: columns of the table
    - raw_data_file: file path containing raw data
    - save_file: file to save table to             
'''
def get_player_stats_tbl(curr_path, columns, raw_data_file):
    #load stats of all players from each season from raw csv
    #keep all columns from raw csv for this table
    player_stats= pd.read_csv(curr_path + '/data/duplicates_removed/' + raw_data_file, 
                               usecols=columns)
    
    #load players.csv to get corresponding player id's for each row
    players_df = pd.read_csv(curr_path + '/data/processed/players.csv', index_col='player_id')

    #create player id column in info df
    player_stats.insert(loc=0, column='player_id', value=0)
    
    #iterate through rows and get correct player id from playerdf and assign to each player instance
    for index, row in players_df.iterrows():
        #get name of player in curren row
        name = row['NAME']
        #select row with column 'NAME' equal to name of player in current row
        #player_row = player_stats.loc[player_stats['NAME'] == name]
        id = index #id is index since it was assigned as the row number in players_df
        #assign id to all rows in player_info with 'NAME' equal to name of player in current row
        player_stats['player_id'].mask(player_stats['NAME'] == name, id, inplace=True)

    #drop NAME column from table so it's not stored in 4 different tables
    # can join with players table if needed
    player_stats = player_stats.drop(['NAME'], axis=1)
    
    return player_stats


def assign_conferences(teams_tbl):
    aus = ['acadia', 'capebreton', 'dalhousie', 'memorial', "saintmarys", 'stfx', 'unb', 'upei']
    rseq = ["bishops", 'concordia', 'laval', 'mcgill', 'uqam']
    oua = ['algoma', 'brock', 'carleton', 'guelph', 'lakehead', 'laurentian', 'laurier', 'mcmaster',
           'nipissing', 'ontariotech', 'ottawa', 'queens', 'ryerson', 'toronto', 'torontometropolitan',
           'waterloo', 'western', 'windsor', 'york']
    canwest = ['alberta', 'brandon', 'calgary', 'lethbridge', 'macewan', 'manitoba', 'mountroyal', 
               'regina', 'saskatchewan', 'thompsonrivers', 'trinitywestern', 'ubc', 'ubcokanagan',
               'ufv', 'unbc', 'victoria', 'winnipeg']
    # create a list of our conditions
    conditions = [
        (teams_tbl['TEAM'].isin(aus)),
        (teams_tbl['TEAM'].isin(rseq)),
        (teams_tbl['TEAM'].isin(oua)),
        (teams_tbl['TEAM'].isin(canwest))
        ]

    # create a list of the values we want to assign for each condition
    values = ['AUS', 'RSEQ', 'OUA', 'CANWEST']

    # create a new column and use np.select to assign values to it using our lists as arguments
    teams_tbl['CONFERENCE'] = np.select(conditions, values)
    
    return teams_tbl

'''
Create table with all team names and team id's
Table Columns: team_id, TEAM
'''
def get_teams_tbl(curr_path):
    #load names of all players from each season from raw csv
    team_names = pd.read_csv(curr_path + '/data/processed/player_info.csv', usecols=['TEAM'])
    #remove duplicate names, only keep one row for each player
    teams_tbl = team_names.drop_duplicates(ignore_index=True)
    
    teams_tbl = assign_conferences(teams_tbl)

    #save to csv file where index is player id
    teams_tbl.to_csv(curr_path + '/data/processed/teams.csv', index=False)
    #teams_tbl.to_csv(curr_path + '/data/tables/teams_test.csv', index=False)


def create_tables(tables, root_path):
    
    if not os.path.exists(root_path + '/data/processed'):
        os.mkdir(root_path + '/data/processed')
    
    for table in tables:
        if table == 'players':
            get_players_tbl(root_path)
        if table == 'player_info':
            columns = ['NAME', 'TEAM', 'SEASON','PLYR_YR', 'NUM', 'GP', 'GS', 'MIN/G']
            raw_data_file = 'player_stats_info.csv'
            save_file = root_path + '/data/processed/player_info.csv'
            #save_file = root_path + '/tables/test_info.csv'
            player_info = get_player_stats_tbl(root_path, columns, raw_data_file)
            
            #replace any strings in NUM column containing non numbers with NaN
            player_info['NUM'] = player_info['NUM'].replace(regex='[!-/:-z]', value=np.nan)
            
            #save table to csv
            player_info.to_csv(save_file, index=False)
            
        if table == 'player_shooting':
            columns = ['NAME', 'SEASON', 'FGM', 'FGA', 'FG%', 
                '3FGM', '3FGA', '3FG%', 'FTM','FTA', 'FT%', 'PPG']
            raw_data_file = 'player_stats_shooting.csv'
            save_file = root_path + '/data/processed/player_shooting.csv'
            #save_file = root_path + '/tables/test_shooting.csv'
            player_shooting = get_player_stats_tbl(root_path, columns, raw_data_file)
            player_shooting.to_csv(save_file, index=False)
            
        if table == 'player_ballcntrl':
            columns = ['NAME', 'SEASON', 'DREB/G', 'OREB/G', 'REB/G', 'PF/G', 'A/G', 'TO/G', 'A/TO', 'STL/G', 'BLK/G']
            raw_data_file = 'player_stats_ball_control.csv'
            save_file = root_path + '/data/processed/player_ballcontrol.csv'
            #save_file = root_path + '/tables/test_bc.csv'
            player_ballcntrl = get_player_stats_tbl(root_path, columns, raw_data_file)
            player_ballcntrl.to_csv(save_file, index=False)
        
        if table == 'teams' and os.path.isfile(root_path + '/data/processed/player_info.csv'):
            get_teams_tbl(root_path)
    
#TODO: create filepath variable for easier code updates