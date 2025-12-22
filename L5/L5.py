# importing libraries
import pandas as pd 
import sqlite3

#  set up connection with database
database = 'database.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql(""" SELECT *
                     FROM sqlite_master
                     WHERE type = 'table';""", conn)

print (tables)

# inner join
joined_city = pd.read_sql(""" SELECT c.Country_Id,
                          c.Country_Name, ci.City_Name
                          FROM country c
                          INNER JOIN city ci
                          ON c.Country_id = ci.Country_Id""", conn)

print(joined_city )

# left outer join
joined_left = pd.read_sql(""" SELECT *
                          FROM Player
                          LEFT JOIN season
                          ON player.Player_ID = season.Man_Of_The_Series
                          """, conn)

print(joined_left)

# cross join
joined_cross = pd.read_sql("""SELECT c.Country_Id,
                           c.Country_Name, ci.City_Name
                           FROM country c
                           CROSS JOIN city ci
                           """, conn)

print(joined_cross)

# union
union = pd.read_sql("""SELECT Player_Name
                    FROM player
                    UNION
                    SELECT Team_Name
                    FROM team
                    """, conn)