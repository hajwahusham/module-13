import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT * FROM sqlite_master
                     WHERE type = 'table';""", conn)
print(tables)

matches = pd.read_sql("""SELECT * FROM match;""", conn)
print(matches.head())

# get average win margin of all winning teams for s9
result1 = pd.read_sql("""SELECT AVG(Win_Margin) AS avg_margin,
                      Match_Winner
                      FROM Match
                      WHERE Season_Id = 9
                      GROUP BY Match_Winner
                      ORDER BY AVG(Win_Margin);""", conn)

print(result1)

# get the count of venues for season 9
result2 = pd.read_sql("""
    SELECT COUNT(DISTINCT Venue_Id) AS venue_count
                      FROM Match
                      WHERE Season_Id = 9;""", conn)

print(result2)

# get minimun, maximum & average win margin
# also get total number of players who recieved man of the match
result3 = pd.read_sql("""SELECT MIN(Win_Margin) AS min_margin,
                      MAX(Win_Margin) AS max_margin,
                      AVG(Win_Margin) AS avg_margin,
                      COUNT(DISTINCT Man_of_the_Match) AS unique_mom_players
                      FROM Match;""", conn)

print(result3)

# return the total win margins for all the winners in s9
result4 = pd.read_sql(""" 
                    SELECT SUM(Win_Margin) AS total_win_margin
                      FROM Match
                      WHERE Season_Id = 9;""", conn)

print(result4)