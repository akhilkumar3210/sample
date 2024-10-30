import mysql.connector

con=mysql.connector.connect(host='localhost',user='myadmin',password='myadmin',database='admin')
con.autocommit=True
cur=con.cursor()
# cur.execute("create database admin")
# cur.execute("create table user(no int,name text,age int)")
# no=int(input("Enter ur No : "))
# name=input("Enter ur Name : ")
# age=int(input("Enter ur Age : "))
# cur.execute("insert into user (no,name,age) values (%s,%s,%s)",(no,name,age))

# cur.execute("select * from user")
# data=cur.fetchall()
# for i in data:
#     print(i)

# name=input("Enter new name :")
# age=int(input("Enter a age : "))
# name1=input("Enter a  old Name : ")
# cur.execute("update user set name=%s,age=%s where name=%s ",(name,age,name1))

# no=int(input("Entet a Number : "))
# cur.execute("delete from user where no=%s",(no,)) 

# cur.execute("select * from user where name like 'a%' ")
# data=cur.fetchall()
# for i in data:
#     print(i)   


# cur.execute("select * from user where name like '______' ")
# data=cur.fetchall()
# for i in data:
#     print(i) 


# cur.execute("select * from user order by name ")
# data=cur.fetchall()
# for i in data:
#     print(i)  

# cur.execute("select * from user order by name  desc ")
# data=cur.fetchall()
# for i in data:
#     print(i)

# cur.execute("create table address(no int,place text,pin int)")

# no=int(input("Enter ur No : "))
# name=input("Enter ur Name : ")
# age=int(input("Enter ur Age : "))
# cur.execute("insert into address (no,place,pin) values (%s,%s,%s)",(no,name,age))


# cur.execute("select user.no,user.name,user.age,address.place,address.pin from user inner join address on user.no=address.no ")
# cur.execute("select user.no,user.name,user.age,address.place,address.pin from user left join address on user.no=address.no ")
# data=cur.fetchall()
# for i in data:
#     print(i)


# cur.execute("select name,min(age) from user group by name")
# cur.execute("select name,max(age) from user group by name")
# cur.execute("select name,sum(age) from user group by name")
# cur.execute("select name,avg(age) from user group by name")
cur.execute("select name,count(age) from user group by name")
data=cur.fetchall()
for i in data:
    print(i)