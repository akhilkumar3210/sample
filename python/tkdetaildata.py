import mysql.connector
con=mysql.connector.connect(host='localhost',user='myadmin',password='myadmin',database='admin')
con.autocommit=True
cur=con.cursor()
# cur.execute("Create table student(id int,name text,age int,gender text)")
cur.execute("select * from student")
data=cur.fetchall()
for i in data:
    print(i)