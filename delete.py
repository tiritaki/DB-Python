from sqliteConnect import *

import read 
from time import sleep

def deleteSongs():
    #songID will be deleted
    idField = input ("enter the ID of the song to be deleted")
    
    #method1
    cursor.execute(f"DELETE FROM songs WHERE SongID = {idField}")
    
    conn.commit()
    print(f"Record {idField} deleted from songs table ")
    sleep(3)
    read.readSongs() 
    
deleteSongs()