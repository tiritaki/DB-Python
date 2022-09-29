import mysql.connector # import the mysqlconnetor
mypass= "yourpassword!"
# connect to mysql server 
"""Create or get a MySQL connection object
In its simpliest form, Connect() will open a connection to
 a MySQL server and return a MySQLConnection object."""
# conn = mysql.connector.connect( host="localhost", user="root", password=mypass)
conn = mysql.connector.connect( host="localhost",database="GLAmusic", user="root", password=mypass)

if conn.is_connected():
    print("Connected to MySQL Server")
else:
    print(" Not Connected!!!")

cursor = conn.cursor(prepared=True)

# create database
# cursor.execute("CREATE DATABASE GLAmusic")