import sqlite3

#create a variable conn and pass sqlite connect
#create a DB file if it is not exist, otherwise will use existing file
conn = sqlite3.connect("/Users/olehpysmenko/Desktop/Projects/DB-Python/GLA1.db") # pass the path and filename inside 

cursor = conn.cursor()