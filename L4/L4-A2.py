## connect with sqlite database
# import neecesasary libraries
import sqlite3
import pandas as pd

# database file
database = 'database.sqlite'

# connect to databse
conn = sqlite3.connect(database)
print("opened database successfullly")

# -------------------------------------------
# display all the tables oof the databaase
df = pd.read_sql("""
                 SELECT * 
                 FROM sqlite_master
                 WHERE type= 'table' ;
                 """, conn)

print(df)

# -------------------------------------------
# display the first 5 rows of player_match table
player_match = pd.read_sql("""
                           SELECT *
                           FROM Player_Match;
                           """, conn)

print(player_match.head())

# -------------------------------------------
# check the presence of null values in player_match table
null_player_match = pd.read_sql("""
                           SELECT *
                           FROM Player_Match
                             WHERE Team_Id IS NULL;
                           """, conn)

print(null_player_match)

# -------------------------------------------
# display the first 5 rows of match table
toss_dec = pd.read_sql("""
                           SELECT *
                           FROM Match;
                           """, conn)

print(toss_dec.head())

# -------------------------------------------
# check the presence of null values in the match table
null_match = pd.read_sql("""
                           SELECT *
                           FROM Match
                            WHERE MATCH_Winner IS NULL;
                           """, conn)
print(null_match)