import mysql.connector
conn = mysql.connector.connect (host='localhost',user='root',password='sasasang12@16')
if conn.is_connected():
    print("connection successful")