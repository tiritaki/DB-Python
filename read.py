from sqliteConnect import *

def readSongs():
    cursor.execute("SELECT * FROM songs") #select all records from songs tabble
    row = cursor.fetchall() #fetch all songs and pass to row variable
    for record in row: #iterate through the records
        print(record)
readSongs()