# importing libraries
import pandas as pd
import sqlite3

# name of the SQLite database file
database = "database.sqlite"

# connecting to database
conn = sqlite3.connect(database)
print("opened database successfully!")

# get list of all the tables
tables = pd.read_sql(""" SELECT name
                     FROM sqlite_master
                     WHERE type = 'table';""", conn)

print("all tables in database:")
print(tables)

# load the team table
teams = pd.read_sql("""SELECT * FROM Team; """, conn)

print("TEam Table (first 5 rows):")
print(teams.head())

# load the 'match' table
matches = pd.read_sql("""SELECT *
                      FROM Match; """, conn)

print("match table (first 5 rows):")
print(matches.head())

# check details of all matches won by Mumbai Indians
# assuming mumbai indians has Team_Id = 7
MI_wins = pd.read_sql("""SELECT *
                      FROM Match
                      WHERE Match_Winner == 7; """, conn)

print("--- all MI wins ---")
print(MI_wins)

# matches won by MI in the last 2 seasons
# assuming its 8 and 9
MI_S8_S9 = pd.read_sql("""SELECT * 
                       FROM Match
                       WHERE Match_Winner == 7 AND Season_Id IN (8, 9);""", conn)

print("--- MI wins in season 8 & 9 ---")
print(MI_S8_S9)

# find teams starting with De
new_teams = pd.read_sql(""" SELECT * 
                        FROM Team
                        WHERE Team_Name LIKE '%De'; """, conn)

print("--- new teams (name starting with De)---")
print(new_teams)

# minimum and maximum winning margin
min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin) AS Min_Margin,
                             MAx(Win_Margin) AS Max_Margin
                             FROM Match; """, conn)

print("--- minimum & maximum winning margin ---")
print(min_max_margin)