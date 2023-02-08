CREATE DATABASE usportsDB;

#to be able to use local option when loading data into tables
SET GLOBAL local_infile = true;  

#create players table and load in data to table
CREATE TABLE players(
	player_id int NOT NULL,
    NAME varchar(50) NOT NULL,
    primary key (player_id)
    );
    
LOAD DATA LOCAL INFILE '/Users/emmaritcey/Documents/basketball_research/usports_database/tables/players.csv' 
INTO TABLE players
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

#create players info table and load data to table
CREATE TABLE player_info(
	row_identifier int NOT NULL,
    NAME varchar(50) NOT NULL,
    TEAM varchar(20) NOT NULL,
    SEASON int NOT NULL,
    PLYR_YR	varchar(10),
    NUM int,
    GP int,
    GS int,
    MIN_G float,
    player_id int NOT NULL,
    PRIMARY KEY (row_identifier),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
    ON DELETE CASCADE #if a player is deleted from players table, then they are deleted from player_info table
    ON UPDATE CASCADE #if a player is updated in players table, then corresponding entries in player_info table are updated
    );
    
LOAD DATA LOCAL INFILE '/Users/emmaritcey/Documents/basketball_research/usports_database/tables/player_info.csv' 
INTO TABLE player_info
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
#if NUM or PLYR_YR entry loaded in as empty string, set value to NULL
(row_identifier, NAME, TEAM, SEASON, @vPLYR_YR, @vNUM, GP, GS, MIN_G, player_id)
SET PLYR_YR = NULLIF(@vPLYR_YR, '');
SET NUM = NULLIF(@vNUM,'');

DROP TABLE player_shooting;

#create players shootings stats table and load data to table
CREATE TABLE player_shooting(
	row_identifier int NOT NULL,
    NAME varchar(50) NOT NULL,
    SEASON int NOT NULL,
    FGM float,
    FGA float,
    FG_PC float,
    FGM3 float,
    FGA3 float,
    FG3_PC float,
    FTM float,
    FTA float,
    FT_PC float,
    PPG float,
    player_id int NOT NULL,
    PRIMARY KEY (row_identifier),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
    ON DELETE CASCADE #if a player is deleted from players table, then they are deleted from player_shooting table
    ON UPDATE CASCADE #if a player is updated in players table, then corresponding entries in player_shooting table are updated
    );
    
LOAD DATA LOCAL INFILE '/Users/emmaritcey/Documents/basketball_research/usports_database/tables/player_shooting.csv' 
INTO TABLE player_shooting
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


#create players ball control stats table and load data to table
CREATE TABLE player_ballcontrol(
	row_identifier int NOT NULL,
    NAME varchar(50) NOT NULL,
    SEASON int NOT NULL,
    DREB_G float,
    OREB_G float,
    REB_G float,
    PF_G float,
    A_G float,
    TO_P float,
    A_TO float,
    STL_G float,
    BLK_G float,
    player_id int NOT NULL,
    PRIMARY KEY (row_identifier),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
    ON DELETE CASCADE #if a player is deleted from players table, then they are deleted from player_ballcontrol table
    ON UPDATE CASCADE #if a player is updated in players table, then corresponding entries in player_ballcontrol table are updated
    );
    
LOAD DATA LOCAL INFILE '/Users/emmaritcey/Documents/basketball_research/usports_database/tables/player_ballcontrol.csv' 
INTO TABLE player_ballcontrol
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
    