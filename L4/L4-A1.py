# connect with sqlite database
# import neecesasary libraries
import sqlite3
import pandas as pd

# connect to databse
conn = sqlite3.connect('database.sqlite')

print("opened database successfullly")
'''
# create a new table in database
conn.execute("""CREATE TABLE CLASS_10
(SNO INT PRIMARY KEY NOT NULL,
ROLL_NO INT NOT NULL,
NAME TEXT NOT NULL,
AGE INT DEFAULT 15,
GENDER TEXT NOT NULL,
EMAIL_ID TEXT NOT NULL,
CONTACT_NO REAL NOT NULL);""")
'''
print("TABLE CREATED SUCCESSFULLY")

# enter data
conn.execute("""INSERT INTO CLASS_10 (SNO, ROLL_NO, NAME, AGE, GENDER, EMAIL_ID, CONTACT_NO)
VALUES(1,1, 'Allen', 14, 'Male', 'allen@gmail.com', 8088900);""")

conn.execute("""INSERT INTO CLASS_10 (SNO, ROLL_NO, NAME, AGE, GENDER, EMAIL_ID, CONTACT_NO)
VALUES(2, 2, 'Aisha', 14, 'Female', 'aisha@gmail.com', 9089000);""")

conn.execute("""INSERT INTO CLASS_10 (SNO, ROLL_NO, NAME, AGE, GENDER, EMAIL_ID, CONTACT_NO)
VALUES(3,3, 'Jeff', 15, 'Male', 'jeff@gmail.com', 8089500);""")

# SAVE CHANGES
conn.commit()
print("Records created successfully")

# display all the tables of this database
tables = pd.read_sql(""" SELECT *
 FROM sqlite_master
 WHERE type = 'table';""", conn)

print(tables)

# read table from the database into a dataframe
class_10d = pd.read_sql("""SELECT *
FROM CLASS_10;""", conn)

print(class_10d.head())