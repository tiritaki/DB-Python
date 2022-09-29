from mysqlConnect import *
def read():
    cursor.execute("SELECT * FROM members")  # select all records from the songs table
    row = (
        cursor.fetchall()
    )  # fetch all the songs that was selected above and pass/store it to the row variable
    for record in row:  # iterate through the records ( held in the row variable)
        print(record)
read()
    