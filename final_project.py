## Final project - IT fundamentals
## By Thinnathee Thanongkiarttisak
## 30 April 2020

## ---------------------------------------
## import sqlite3 library
import sqlite3

## connect to database
conn = sqlite3.connect("university.db")

## create cursor to execute our queries
cur = conn.cursor()

## write our queries
sql = "select * from student limit 5;"

## fetch data
cur.execute(sql)
result = cur.fetchall()

## print result in console
for row in result:
    print(row)
conn.close()