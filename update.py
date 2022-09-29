from sqliteConnect import *
from time import sleep

import read

def updateSongs():
    # songID to be updated
    idField = input("Enter the ID of the song to be updated: ")
    # Enter the name of the field to be updated
    fieldName = input(
        "Which field would you like to update? (Title, Artist or Genre): "
    ).title()
    # Enter the value of the field to be updated
    newFieldValue = input(f"Enter the new field value for {fieldName} ")
    print(f"The new field value entered is: {newFieldValue}")

    # add a single quote to the new field value 
    # name = Anna , now name = "'" + Anna + "'" = 'Anna'
    newFieldValue = "'" + newFieldValue + "'"
    print(f"Amended new field value entered is: {newFieldValue}")

    cursor.execute(F"UPDATE songs SET {fieldName} = {newFieldValue} WHERE SongID = {idField }")
    conn.commit()
    print(f"Record {idField} updated in songs table")
    sleep(3)
    read.readSongs()  # invoke the subroutine readSongs from read.py

updateSongs()