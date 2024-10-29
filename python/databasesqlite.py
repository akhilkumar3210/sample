import sqlite3
con=sqlite3.connect("usdatabase.db")
try:
    con.execute("create table user(no int,name text,age int)")
except:
    print("table created")
# con.execute("insert into user(no,name,age)values(1,'athul',21),(2,'deepu',21)")
# con.execute("insert into user(no,name,age)values(3,'neeraj',21),(4,'nabeel',20)")
# con.commit()

# no=int(input("Enter ur No : "))
# name=input("Enter ur Name : ")
# age=int(input("Enter ur Age : "))
# con.execute("insert into user(no,name,age)values(?,?,?)",(no,name,age))
# con.commit()


# limit=int(input("Enter Limit : "))
# for i in range(limit):
#     no=int(input("Enter ur No : "))
#     name=input("Enter ur Name : ")
#     age=int(input("Enter ur Age : "))
#     con.execute("insert into user(no,name,age)values(?,?,?)",(no,name,age))
#     con.commit()
# no=input("Enter a Name : ")
# data=con.execute("select * from user where name=?",(no,))
# print('{:<10}{:<20}{:<30}'.format('No','Name','Age'))
# print('-'*35)
# for i in data:
#     print('{:<10}{:<20}{:<30}'.format(i[0],i[1],i[2]))

# name=input("Enter new name :")
# age=int(input("Enter a age : "))
# name1=input("Enter a  old Name : ")
# con.execute("update user set name=?,age=? where name=? ",(name,age,name1))
# con.commit()
# no=int(input("Entet a Number : "))
# con.execute("delete from user where no=?",(no,))
# con.commit()

# data=con.execute("select * from user where name like '%u' ")
# data=con.execute("select * from user where name like '______' ")

# data=con.execute("select * from user order by name ")
# data=con.execute("select * from user order by name  desc ")
# for i in data:
#     print(i)

try:
    con.execute("create table address(no int,place text,pin int)")
except:
    print("table created ")

# con.execute("insert into user(no,name,age)values(1,'jerin',32)")
# con.commit()
#data=con.execute("select user.no,user.name,user.age,address.place,address.pin from user inner join address on user.no=address.no ")
# data=con.execute("select user.no,user.name,user.age,address.place,address.pin from user left join address on user.no=address.no ")
# data=con.execute("select user.no,user.name,user.age,address.place,address.pin from user left join address on user.no=address.no ")
# for i in data:
#     print(i)

# data=con.execute("select name,min(age) from user group by name")
# data=con.execute("select name,max(age) from user group by name")
# data=con.execute("select name,sum(age) from user group by name")
# data=con.execute("select name,avg(age) from user group by name")
data=con.execute("select name,count(age) from user group by name")
for i in data:
    print(i)