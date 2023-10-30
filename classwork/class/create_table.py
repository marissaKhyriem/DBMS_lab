import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='sasasang12@16')
mycursor=conn.cursor()
mycursor.execute("create table if not exists testdb.student(name varchar(100),Rollno int(5),Age int(2),mark float);")
conn.close()
