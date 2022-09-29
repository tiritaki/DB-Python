from re import search
from mysqlConnect import *
import time

def searchMember():
    # Field to search
    searchField = input("Which field would you like to search?(Firstname, Lastname or Email): ").title()
    # Enter the name of the field to be updated

     # Enter the value of the field to be updated
    searchValue = input(f"Enter the value for {searchField} ")
    print(f"The new field value entered is: {searchValue}")

    # artist = MJ = "'" + MJ + "'" = 'MJ'
    searchValue = "'" +searchValue+ "'"
    print(f"Amended search value is: {searchValue}")

    # search the database
    "Select * FROM members WHERE Firstname/Lastname/Email {searchField}  = {searchValue}"
    "Select * FROM members WHERE Firstname = Abdul"
    #Method 1
    cursor.execute(f"Select * FROM members WHERE {searchField}  = {searchValue}")
    time.sleep(3)

    row = cursor.fetchall()
    # convert/cast 

    strRow = str(row)
    if searchValue in strRow:
        for record in row:
            print(record)
    else:
        print(f"The field {searchField} does not contain {searchValue} in the db")

searchMember()




