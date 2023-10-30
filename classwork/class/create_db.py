import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='sasasang12@16')
mycursor=conn.cursor()
mycursor.execute("create database if not exists testdb")
conn.close()