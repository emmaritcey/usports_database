
import numpy as np

'''helper functions to perform scraping'''

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
    makes = float(makes_atts[0])
    attempts = float(makes_atts[1])
    return makes, attempts

'''
remove \n chars from names and for names with errors (repeating chars forever), just use first three letters of first/last name
'''
def parse_name(string):
    temp_list = string.split(' ') #split into list, each ' ' is separate entry
    name = ''
    fn_flag = 0
    for idx in range(len(temp_list)): #loop through list, select first and last name, remove \n chars, 
        if len(temp_list[idx]) > 0 and temp_list[idx]!='\n\n' and temp_list[idx] != '\n':
            #check for upper limit as there are some text errors which cause super long strings (only a few cases)
            if len(temp_list[idx]) > 50:  #just use first three letters of first name
                end_idx = 4
            else:
                end_idx = -1
                  
            if fn_flag:
                name = name + ' ' + temp_list[idx][0:end_idx] #add space bw first and last, remove \n from end of text
            else:
                name = temp_list[idx][0:end_idx] #remove \n from end of text
                fn_flag = 1
    return name