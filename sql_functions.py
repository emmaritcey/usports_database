#functions obtained from: https://www.freecodecamp.org/news/connect-python-with-sql/
#import these functions to other files to use all the time

import mysql.connector 
from mysql.connector import Error
import pandas as pd

'''
function to establish connection to MySQL server
use when database has not yet been created
'''
def create_server_connection(host_name, user_name, user_password):
    connection = None #close any existing connections
    try: 
        #create connection to server
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}")
        
    return connection


'''
function to create SQL database
connection: connection object we created
query: SQL query to execute in the server via the connection
'''
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}")
        

'''
function to connect to server and to a database that's already been created
'''
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name,
            allow_local_infile = True
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}")
    
    return connection


'''
function to execute any SQL query
store queries as strings and pass to cursor.execute() to execute them on the server
'''
def execute_query(connection, query, multi_statement=False):
    cursor = connection.cursor()
    try:
        cursor.execute(query, multi=multi_statement)
        connection.commit() #make sure query is implemented
        print("Query succesful")
    except Error as err:
        print(f"Error: '{err}")
        
        
'''
function to read data from the data (for queries like SELECT)
'''
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")