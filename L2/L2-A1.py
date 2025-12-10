import pandas as pd
import sqlite3

database = 'database.db'
conn = sqlite3.connect(database)

# read sql query for getting all the tables of database intp a dataframe
tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type = 'table';""", conn)

print(tables)
print("-----------------------")

df = pd.read_sql("""SELECT * FROM Salesman;""", conn)
print(df)
print("-----------------------")

df1 = pd.read_sql("""SELECT * FROM Salesman
                  WHERE city LIKE '%e';""", conn)

print(df1)
print("-----------------------")
print(df1.dtypes)
print("-----------------------")
print(df1.columns)
print("-----------------------")


df2 = pd.read_sql("""SELECT SUM(comission) as total_comission FROM Salesman
                  WHERE comission > 0.12; """, conn)

print(df2)
print("-----------------------")