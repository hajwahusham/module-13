# importing libraries
import pandas as pd  
import numpy as np

import sqlite3

database= 'database.sqlite'

conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type= 'table';""", conn)

print(tables)

# fetch all details of matches played by CSK in 2015
csk_matches_2015 = pd.read_sql("""SELECT Match_Id, Team_2 AS Away_Team, Toss_Winner, Match_Winner
                               FROM Match
                               WHERE Team_1 =
                               (SELECT Team_1
                               FROM Match
                               WHERE Team_1 == 3 AND Season_Id == 8);""", conn)

print("matches playes by chennai super kings in 2015")
print(csk_matches_2015)

# fetch details of all matches played by csk inn 2015
csk_wins = pd.read_sql("""SELECT *
                       FROM MATCH
                       WHERE Match_Winner == 3 AND Season_Id == 8;""", conn)

print("\n Matches won by csk as home team in 2015")
print(csk_wins)

# fetch details of all matches
# wher batsman score more than 5 in 2015
match_runs = pd.read_sql(""" SELECT Match_Id, Runs_Scored AS Total_Runs, Innings_No
                         FROM Batsman_Scored
                         WHERE Total_Runs > 5 AND Match_Id IN
                         (SELECT Match_id
                         FROM Match
                         WHERE Season_ID == 8)""", conn)

print("\n matches with scored runs greater than 5 in 2015")
print(match_runs)

# fetch details of matches played in 2015
# where total runs scored where greater than average scored run
avg_runs = pd.read_sql("""SELECT Match_Id, Runs_Scored AS Total_Runs, Innings_No
                       FROM Batsman_Scored
                       WHERE Innings_No == 1 AND Runs_Scored >
                       (SELECT AVG(Runs_Scored)
                       FROM Batsman_Scored)""", conn)

print("\n matches scored runs greater than average scored runs")
print(avg_runs)