#%%
#This notebook contains examples of some typical queries used to find statistical leaders and 
# trends in USports women's basketball since the 2009-2010 season
#Results usually output in a dataframe 

#%%
import pandas as pd
from sql_functions import create_db_connection, execute_query, read_query

#%%
#connect to database to start
pw = "Queens2021!"
connection = create_db_connection("localhost", "root", pw, "usports")
# %%
#get highest average for a stat for each season for players playing more than 10 games
q = """
    SELECT max(ppg), player_shooting.season
    FROM players 
    JOIN player_shooting 
    ON players.player_id = player_shooting.player_id
    JOIN player_info
    ON player_shooting.player_id = player_info.player_id AND
       player_shooting.season = player_info.season
    WHERE games_played > 10
    GROUP BY player_shooting.season
    ORDER BY player_shooting.season
    """
result = read_query(connection, q, None)
result
df = pd.DataFrame(result)
df
# %%
# find the player who recorded highest average for a stat for each season (who played more than 10 games)
g_played = 10
for t in result:
    t_ppg = t[0]-0.1
    t_season = t[1]
    vars = [t_ppg, t_season, g_played]

    q = """
        SELECT name, ppg, player_shooting.season
        FROM players 
        JOIN player_shooting 
        ON players.player_id = player_shooting.player_id
        JOIN player_info
        ON player_shooting.player_id = player_info.player_id AND
           player_shooting.season = player_info.season
        WHERE ppg > %s AND player_shooting.season = %s AND games_played > %s
        ORDER BY player_shooting.season;
        """
    query_result = read_query(connection, q, vars)
    print(query_result)

# %%
#get player id of players who recorded certain statistical milestones (as well as the statistics themselves)
q = """
    SELECT player_shooting.player_id, ppg, reb
    FROM player_shooting 
    JOIN player_ballcontrol
    ON player_shooting.player_id = player_ballcontrol.player_id 
    AND player_shooting.season = player_ballcontrol.season
    JOIN player_info
    ON player_shooting.player_id = player_info.player_id
    AND player_shooting.season = player_info.season
    WHERE ppg > 20 AND reb > 10 AND games_played > 10;
    """
query_result = read_query(connection, q, None)
df = pd.DataFrame(query_result, columns=['Player ID', 'PPG', 'Rebounds'])
df
# %%
#get name and player id of those who recorded certain statistical milestones in a season
q = """
    SELECT name, player_id
    FROM players
    WHERE player_id IN (SELECT player_shooting.player_id
                        FROM player_shooting 
                        JOIN player_ballcontrol
                        ON player_shooting.player_id = player_ballcontrol.player_id 
                        AND player_shooting.season = player_ballcontrol.season
                        JOIN player_info
                        ON player_shooting.player_id = player_info.player_id
                        AND player_shooting.season = player_info.season
                        WHERE ppg > 20 AND reb > 10 AND games_played > 10);
    """
    
query_result = read_query(connection, q, None)
df = pd.DataFrame(query_result)
df


# %%
#get name, player id, season, and team of players who recorded certain statistical milestones
# - an alternative to the method above to return more information and players who achieved milestone multiple times
q = """
    SELECT name, player_id, season, team
    FROM players 
    NATURAL JOIN player_shooting 
    NATURAL JOIN player_ballcontrol
    NATURAL JOIN player_info
    WHERE ppg > 20 AND reb > 10 AND games_played > 10;
    """                  

query_result = read_query(connection, q, None)
df = pd.DataFrame(query_result)
df
# %%
#Count number of seasons each player achieved the statistical milestones
q = """
    SELECT name, count(name)
    FROM players 
    NATURAL JOIN player_shooting 
    NATURAL JOIN player_ballcontrol
    NATURAL JOIN player_info
    WHERE ppg > 20 AND reb > 10 AND games_played > 10
    GROUP BY name;
    """                  

query_result = read_query(connection, q, None)
df = pd.DataFrame(query_result)
df
# %%
#get highest average for a stat for each jersey number for players playing more than 10 games
q = """
    SELECT max(ppg), number
    FROM players 
    NATURAL JOIN player_shooting 
    NATURAL JOIN player_info
    WHERE games_played > 10
    GROUP BY number
    ORDER BY number;
    """
result = read_query(connection, q, None)
result
df = pd.DataFrame(result)
df

# %%
# find the player who recorded highest average for each jersey number (who played more than 10 games)
g_played = 10
idx = 0
for t in result:
    if idx == 0: #skip None Number
        idx += 1
        continue
    t_stat = t[0]-0.1
    t_group = t[1]
    vars = [t_stat, t_group, g_played]

    q = """
        SELECT name, ppg, player_info.number
        FROM players 
        NATURAL JOIN player_shooting 
        NATURAL JOIN player_info
        WHERE ppg > %s AND player_info.number = %s AND games_played > %s;
        """
    query_result = read_query(connection, q, vars)
    print(query_result)
    

# %%
# count number of players who took greater than X three pointers in each season
q = """
    SELECT season, count(name)
    FROM players
    NATURAL JOIN player_shooting
    WHERE fga3 > 6
    GROUP BY season;
    """

result = read_query(connection, q, None)
result
df = pd.DataFrame(result)
df
# %%
# count number of players who averaged over 35% 3FG and took at least 2 per game in each season
q = """
    SELECT season, count(name)
    FROM players
    NATURAL JOIN player_shooting
    WHERE fga3 > 2 AND fg3_percent > 35
    GROUP BY season;
    """

result = read_query(connection, q, None)
result
df = pd.DataFrame(result)
df
# %%
