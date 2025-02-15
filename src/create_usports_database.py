from sqlUtils.sql_functions import create_server_connection, create_database, create_db_connection, execute_query


def initialize_database():
    #create connection
    pw = "******" #enter password to root
    connection = create_server_connection("localhost", "root", pw)
    
    #create usports database
    create_database_query = "CREATE DATABASE usports" 
    create_database(connection, create_database_query) 
    
    #connect to usports database
    connection = create_db_connection("localhost", "root", pw, "usports")
    
    return connection


def create_entities(connection):
    #use triple quote notations for multi-line strings to store SQL queries to make then more readable
    create_player_table = """
        CREATE TABLE players(
            player_id int NOT NULL,
            NAME varchar(50) NOT NULL,
            PRIMARY KEY (player_id, NAME)
            );
        """
    create_teams_table = """
        CREATE TABLE teams(
            name varchar(20) NOT NULL,
            conference varchar(10),
            PRIMARY KEY (name)
            );
        """
    create_player_info_table ="""
        CREATE TABLE player_info(
            player_id int NOT NULL,
            team varchar(20) NOT NULL,
            season int NOT NULL,
            player_year	varchar(10),
            number int,
            games_played int,
            games_started int,
            minutes_pgame float,
            PRIMARY KEY (player_id, season),
            FOREIGN KEY (team) REFERENCES teams(name),
            FOREIGN KEY (player_id) REFERENCES players(player_id)
            ON DELETE CASCADE #if a player is deleted from players table, then they are deleted from player_info table
            ON UPDATE CASCADE #if a player is updated in players table, then corresponding entries in player_info table are updated
            );
        """
    create_player_shooting_table = """
        CREATE TABLE player_shooting(
            player_id int NOT NULL,
            season int NOT NULL,
            fgm float,
            fga float,
            fg_percent float,
            fgm3 float,
            fga3 float,
            fg3_percent float,
            ftm float,
            fta float,
            ft_percent float,
            ppg float,
            PRIMARY KEY (player_id, season),
            FOREIGN KEY (player_id) REFERENCES players(player_id)
            ON DELETE CASCADE #if a player is deleted from players table, then they are deleted from player_shooting table
            ON UPDATE CASCADE #if a player is updated in players table, then corresponding entries in player_shooting table are updated
            );
        """
    create_player_ballcontrol_table = """
        CREATE TABLE player_ballcontrol(
            player_id int NOT NULL,
            season int NOT NULL,
            dreb float,
            oreb float,
            reb float,
            pf float,
            apg float,
            topg float,
            a_to_ratio float,
            spg float,
            bpg float,
            PRIMARY KEY (player_id, season),
            FOREIGN KEY (player_id) REFERENCES players(player_id)
            ON DELETE CASCADE #if a player is deleted from players table, then they are deleted from player_ballcontrol table
            ON UPDATE CASCADE #if a player is updated in players table, then corresponding entries in player_ballcontrol table are updated
            );
    """
    
    create_team_splitstats_table = """
        CREATE TABLE team_splitstats(
            season int NOT NULL,
            team varchar(20) NOT NULL,
            split varchar(15) NOT NULL,
            games_played int,
            fgm float,
            fga float,
            fg_percent float,
            fgm3 float,
            fga3 float,
            fg3_percent float,
            ftm float,
            fta float,
            ft_percent float,
            dreb float,
            oreb float,
            reb float,
            apg float,
            topg float,
            spg float,
            bpg float,
            pf float,
            ppg float,
            off_eff float,
            net_eff float,
            PRIMARY KEY (season, team, split),
            FOREIGN KEY (team) REFERENCES teams(name)
            ON DELETE CASCADE #if a team is deleted from teams table, then they are deleted from team_splitstats table
            ON UPDATE CASCADE #if a team is updated in teams table, then corresponding entries in team_splitstats table are updated
            );
    """
    
    create_allstars_table ="""
        CREATE TABLE allstars(
            season int NOT NULL,
            NAME varchar(50) NOT NULL,
            team varchar(20) NOT NULL,
            conference varchar(10),
            allstar_team int NOT NULL,
            PRIMARY KEY (season, NAME, team)
            #ON DELETE CASCADE #if a player is deleted from players table, then they are deleted from allstars table
            #ON UPDATE CASCADE #if a player is updated in players table, then corresponding entries in allstars table are updated
            );
    """
    
    execute_query(connection, create_player_table)
    execute_query(connection, create_teams_table)
    execute_query(connection, create_player_info_table)
    execute_query(connection, create_player_shooting_table)
    execute_query(connection, create_player_ballcontrol_table)
    execute_query(connection, create_team_splitstats_table)
    execute_query(connection, create_allstars_table)


def populate_entities(connection):
    load_players = """
        LOAD DATA LOCAL INFILE '/Users/emmaritcey/Documents/basketball_research/usports_database/data/processed/players.csv' 
        INTO TABLE players
        FIELDS TERMINATED BY ',' 
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;
    """
    
    load_teams = """
        LOAD DATA LOCAL INFILE '/Users/emmaritcey/Documents/basketball_research/usports_database/data/processed/teams.csv'
        INTO TABLE teams
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;
        """

    # if player year or number entry is loaded in as empty string, set value to NULL
    load_player_info = """
        LOAD DATA LOCAL INFILE '/Users/emmaritcey/Documents/basketball_research/usports_database/data/processed/player_info.csv' 
        INTO TABLE player_info
        FIELDS TERMINATED BY ',' 
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS
        (player_id, team, season, @vplayer_year, @vnumber, games_played, games_started, minutes_pgame)
        SET player_year = NULLIF(@vplayer_year, ''),
            number = NULLIF(@vnumber,'');
        """
        
    load_player_shooting = """
        LOAD DATA LOCAL INFILE '/Users/emmaritcey/Documents/basketball_research/usports_database/data/processed/player_shooting.csv' 
        INTO TABLE player_shooting
        FIELDS TERMINATED BY ',' 
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;
        """

    load_player_ballcontrol = """
        LOAD DATA LOCAL INFILE '/Users/emmaritcey/Documents/basketball_research/usports_database/data/processed/player_ballcontrol.csv' 
        INTO TABLE player_ballcontrol
        FIELDS TERMINATED BY ',' 
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;
        """
    
    load_team_splitstats = """
        LOAD DATA LOCAL INFILE '/Users/emmaritcey/Documents/basketball_research/usports_database/data/raw/team_splitstats.csv'
        INTO TABLE team_splitstats
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;
        """
        
    load_allstars = """
        LOAD DATA LOCAL INFILE '/Users/emmaritcey/Documents/basketball_research/usports_database/data/processed/all_stars.csv'
        INTO TABLE allstars
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;
        """
        
    execute_query(connection, load_players)
    execute_query(connection, load_teams)
    execute_query(connection, load_player_info)
    execute_query(connection, load_player_shooting)
    execute_query(connection, load_player_ballcontrol)
    execute_query(connection, load_team_splitstats)
    execute_query(connection, load_allstars)


def setupDB():
    #connect to server and create database
    connection = initialize_database()
    
    #set variable to be able to use local option when loading data into tables
    set_restrictions = "SET GLOBAL local_infile = true;"
    execute_query(connection, set_restrictions)
    
    #create all tables for database
    create_entities(connection)
    
    #populate entities with data from csv files
    populate_entities(connection)



def main():
    setupDB()

    
if __name__ == "__main__":
    main()


#TODO: change so that database name is instantiated in main so it's more easilty changed