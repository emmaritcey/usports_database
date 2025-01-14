# USports Women's Basketball Data
This repository contains code to analyze and visualize USports women's basketball data.
Code includes scraping data from USports women's basketball website, saving raw data into csv files, cleaning data into new csv files, creating a relational database

[(Back to top)](#usports-womens-basketball-data)

# Table of Contents

- [USports Women's Basketball Data](#usports-womens-basketball-data)
- [Table of Contents](#table-of-contents)
- [Technologies Used](#technologies-used)
- [Setup/Installation Requirements](#setupinstallation-requirements)
- [Data](#data)
    - [Collection](#collection)
    - [SQL Database Creation](#sql-database-creation)
- [Code Structure](#code-structure)


[(Back to top)](#table-of-contents)

## Technologies Used
* Python 
* SQL

[(Back to top)](#technologies-used)

## Setup/Installation Requirements
The only requirements for this code are a computer, internet connection, and Python 3.0 or above
To install required libraries, run: 
```bash
pip install -r requirements.txt
```

[(Back to top)](#setupinstallation-requirements)

## Data

### Collection
The data for this project is obtained from USports (https://universitysport.prestosports.com/sports/wbkb/)
To scrape individual player data run:
```bash
scrape_data.py
```
This script:
* scrapes individual and team data from USports website and saves raw data into csv files (when scrape = 1). Files saved in data/raw_csv_files:
    * players_stats_ball_control.csv
    * player_stats_info.csv
    * player_stats_shooting.csv
    * team_splitstats.csv
* cleans data and creates separate tables saved as csv files (when clean = 1) for use in a relational database. Files saved in data/processed:
    * player_ballcontrol.csv
    * player_info.csv
    * player_shooting.csv
    * players.csv
    * teams.csv
* player_info data: missing values in 'NUM' and 'PLYR_YR' columns set to np.nan, missing data ('-') of numeric column set to 0
* boolean variables at beginning of main function determine what data to scrape/clean
* calls any of ***scrape_player_data.py, scrape_team_data.py, and/or clean_data.py*** based on these variables

### SQL Database Creation
To create a relational database of the data in data/processed, run: 
```bash
create_usports_database.py
```
This script:
* uses functions in ***src/utils/sql_functions.py ***
* takes the data from the csv files in data/processed folder (created with create_player_tables.py)
* Folder titled 'sql_code' contains .sql files created prior to moving over to python (not up to date)

[(Back to top)](#data)


## Code Structure
```bash
├── data
│   ├── processed
│       ├── player_ballcontrol.csv
|       ├── player_info.csv
|       ├── player_shooting.csv
|       ├── players.csv
|       └── teams.csv
│   ├── raw
|       ├── player_stats_ball_control.csv
|       ├── player_stats_info.csv
|       ├── player_stats_shooting.csv
|       └── team_splitstats.csv
├── images
├── notebooks
|   ├── Visualizations_Rebounding.ipynb
|   └── Visualizations_Scoring.ipynb
├── sql_code
├── src
|   ├── data
|       ├── preprocessUtils
|           ├── clean_data.py
|           ├── scrape_player_data.py
|           ├── scrape_team_data.py
|           └── scraping_helpers.py
|       ├── collect_data.py
|       └── create_usports_database.py
|   └── utils
|       └── sql_functions.py
├── .gitignore
├── README.md
└── requirements.txt
```

[(Back to top)](#code-structure)


