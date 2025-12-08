import pandas as pd  
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print ("opened successfully")

# read sql query for getting all the tables of database into a dataframe
tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type = 'table'; """, conn)

print (tables)