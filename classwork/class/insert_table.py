import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='sasasang12@16')
mycursor=conn.cursor()
mycursor.execute("insert into testdb.student values('Harry',21,22,82.5);")
mycursor.execute("insert into testdb.student values('Larry',20,22,85);")
mycursor.execute("insert into testdb.student values('Garry',22,22,92);")
conn.commit()
conn.close()