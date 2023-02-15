#%%
import pandas as pd
from sql_functions import create_db_connection, execute_query, read_query
#connect to database to start
pw = "Queens2021!"
connection = create_db_connection("localhost", "root", pw, "usports")
# %%
#get highest ppg average for each season for players playing more than 10 games
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
# find the player who scored the highest ppg for each season
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
q = """
    SELECT ppg
    FROM player_info
    WHERE number = 34;
    """
query_result = read_query(connection, q, None)
df = pd.DataFrame(query_result)
df
# %%
list(df[0])

