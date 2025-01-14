
import numpy as np
import pandas as pd
from selenium.webdriver.common.by import By


'''helper functions to perform scraping'''


'''
function scrapes the rows from a table pulled from usports website
table_columns are the names of the columns in the table
'''
def scrape_table_rows(rows, table_columns):
    # Scrape data from each row
    df = pd.DataFrame(columns = table_columns)
    for row in rows:
        # Get each cell (td) in the row
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells]
        if row_data:  # Skip empty rows
            row_data = pd.DataFrame([row_data], columns = table_columns)
            df = pd.concat([df, row_data], ignore_index=True)
    
    return df


'''
values in tables come with a space before and after
this function removes the space
'''
def parse_values_team(string):
    temp_list = string.split(' ') #split into list, each ' ' is separate entry
    for idx in range(len(temp_list)): #loop through list, select first and last name, remove \n chars
        if len(temp_list[idx]) > 0 and temp_list[idx] != '\n':
            value = temp_list[idx] #remove \n from end of text
    try:
        if value == '-':
            value = 0
    except:
        value = np.nan
        
        
    return value

'''
parse values from player data to remove spaces and \n chars
'''
def parse_values_player(string):
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


'''
shooting stats are a string: 'fgm-fga'
this function separates fgm from fga to two separate floats
'''
def parse_shooting(fraction_str):
    makes_atts = fraction_str.split('-')
    makes = int(makes_atts[0])
    attempts = int(makes_atts[1])
    return makes, attempts

'''
remove \n chars from names and for names with errors (repeating chars forever), just use first three letters of first/last name
'''
def parse_name(string, teams):
    temp_list = string.split(' ') #split into list, each ' ' is separate entry
    name = ''
    fn_flag = 0
    team_flag = 0
    for idx in range(len(temp_list)): #loop through list, select first and last name, remove \n chars, 
        if len(temp_list[idx]) > 0 and temp_list[idx]!='\n\n' and temp_list[idx] != '\n' and temp_list[idx] != '\n\n\n':
            #check for upper limit as there are some text errors which cause super long strings (only a few cases)
            if len(temp_list[idx]) > 50:  #just use first three letters of first name
                end_idx = 4
            else:
                end_idx = -1
                  
            if fn_flag: #last name
                last_name = temp_list[idx][0:]
                if last_name[-1] == '\n':
                    last_name = last_name[0:end_idx]
                if team_flag and (last_name.lower() == 'team' or last_name.lower() in teams):
                    name = ''
                else:
                    name = name + ' ' + last_name #add space bw first and last, remove \n from end of text 
            else: #first name
                name = temp_list[idx][0:] #remove \n from end of text
                if name[-1] == '\n':
                    name = name[0:end_idx]
                if name.lower() == 'team' or name.lower() in teams:
                    team_flag = 1
                
            fn_flag = 1
                
    return name