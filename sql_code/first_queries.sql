#file to get more comfortable with lots of different types of queries

#select all columns from table player_shooting
SELECT * FROM player_shooting;

#get player id of every player who scored more than 20 points per game
SELECT player_id, season FROM player_shooting
WHERE PPG > 20;

#match tuples (rows) with the same values for all common attributes/columns
#retains only one column for each common atrribute
#in this case, common attribute is player_id. In this case, lists all of the players shooting stats (as in player_shooting) and their name (from players)
SELECT * FROM players NATURAL JOIN player_shooting;

#select each unique player name instance
SELECT DISTINCT name FROM players;

#select each unique player name and order alphabetically by name
SELECT DISTINCT name 
FROM players
ORDER BY name;

#select each player and year they played, ordered by season and alphabetically by name
SELECT name, season 
FROM players 
NATURAL JOIN player_shooting
ORDER BY season, name;

#select each player, their ppg, and the season
#order alphabetically by name, then by descending ppg (default is ascending)
SELECT name, ppg, season
FROM players
NATURAL JOIN player_shooting
ORDER BY name, ppg DESC;

#get average individual ppg across all players in 2012
SELECT avg(ppg)
FROM player_shooting
WHERE season = 2012;

#get the number of players in 2019 that scored more than 5 ppg
SELECT count(ppg)
FROM player_shooting
WHERE season = 2019 and ppg > 5;

#get the average individual ppg across all players in each season
SELECT season, avg(ppg)
FROM player_shooting
GROUP BY season;

#get seasons and their average ppg, only for seasons with an average ppg greater than 5.1
#** having clause is applied AFTER the group by, where clause is applied BEFORE the group by
SELECT season, avg(ppg)
FROM player_shooting
GROUP BY season
HAVING avg(ppg) > 5.1;

#nested queries

#find player id's of players who played in both 2014 and 2016
SELECT player_id
FROM player_shooting
WHERE season = 2014 AND
	player_id IN(SELECT player_id
				FROM player_shooting
				WHERE season = 2016);

#find player names of players who played in both 2014 and 2016
SELECT name
FROM player_shooting NATURAL JOIN players
WHERE season = 2014 AND
	name IN(SELECT name
				FROM player_shooting NATURAL JOIN players
				WHERE season = 2016);

#find player names of players who played in 2014 but not in 2015
SELECT name
FROM player_shooting NATURAL JOIN players
WHERE season = 2014 AND
	name NOT IN(SELECT name
				FROM player_shooting NATURAL JOIN players
				WHERE season = 2015);
                
#count the number of players who played in 2014 but not in 2015
SELECT count(name)
FROM player_shooting NATURAL JOIN players
WHERE season = 2014 AND
	name NOT IN(SELECT name
				FROM player_shooting NATURAL JOIN players
				WHERE season = 2015);
                
SHOW TABLES;