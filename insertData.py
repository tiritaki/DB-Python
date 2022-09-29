from sqliteConnect import *
from time import sleep
from read import *
# create a subrutine to add songs in DB
def addSongs():
    #create an empty list
    songs = []
    
    # capture user data
    title = input ("enter song title")
    artist = input ("enter artist: ")
    genre = input ("enter song genre: ")
    
    #append data capture into the song list
    #song id is set as autoincrement
    songs.append(title)
    songs.append(artist)
    songs.append(genre)
    
    #insert data from appended list
    cursor.execute("INSERT INTO songs VALUES (NULL, ?, ?, ?)", songs)
    conn.commit() #commit changes permanently to DB songs
    print(f"{title} added to the songs table")
    sleep(3) #delay three seconds 
    readSongs()
    
    # cursor.execute("SELECT * FROM songs") #select all records from songs tabble
    # row = cursor.fetchall() #fetch all songs and pass to row variable
    # for record in row: #iterate through the records
    #     print(record)
        
addSongs() #call subrutine