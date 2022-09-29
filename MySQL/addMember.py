from mysqlConnect import *
from readMembers import read
from time import sleep

# create a subroutine to add songs to the songs table in the database GLA1.db
def addMembers():
    # create an empty list
    members = []

    # capture user data
    fname= input("Enter Firstname: ")
    lname = input("Enter Lastname: ")
    email= input("Enter Email: ")

    # append data capture above from the user into the song list []
    "songs.SongID is set as autoincrement  and would be added automatically"
    # listname.append(variable)
    members.append(fname)
    members.append(lname)
    members.append(email)
  # insert data appended to the list above into the songs table
    cursor.execute("INSERT INTO members VALUES(NULL, %s, %s, %s)", members)
    conn.commit()  # commit/write changes permanently to the table songs
    print(
        f"{fname} added to the members table"
    )  # display the name of the song that was added
    sleep(3)  # delay three second before executing the next line of code
    read()

    # cursor.execute("SELECT * FROM members")  # select all records from the songs table
    # row = (
    #     cursor.fetchall()
    # )  # fetch all the songs that was selected above and pass/store it to the row variable
    # for record in row:  # iterate through the records ( held in the row variable)
    #     print(record)


addMembers()  # call/invoke addSongs subroutine
