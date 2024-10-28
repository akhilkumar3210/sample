import sqlite3
cont=sqlite3.connect("ems.db")
try:
    cont.execute("create table employee(empid int,name text,position text)")
except:
    print("created tablee")
    
while True:
    print(''' 
          1.Insert
          2.View
          3.Update
          4.Delete
          5.Exit
          ''')
    choice=int(input("Enter a choice : "))
    if choice==1:
        empid=int(input("Enter ur Empid : "))
        name=input("Enter ur Name : ")
        position=input("Enter ur position : ")
        cont.execute("insert into employee(empid,name,position)values(?,?,?,?)",(empid,name,position))
        cont.commit()
    elif choice==2:
        data=cont.execute("select * from employee")
        print('{:<10}{:<20}{:<20}'.format('Empid','Name','Position'))
        print('-'*40)
        for i in data:
            print('{:<10}{:<20}{:<20}'.format(i[0],i[1],i[2]))
    elif choice==3:
        name=input("Enter new name :")
        position=input("Enter new position  : ")
        name1=input("Enter a  old Name : ")
        cont.execute("update employee set name=?,position=? where name=? ",(name,position,name1))
        cont.commit()
    elif choice==4:
        empid=int(input("Entet empid : "))
        cont.execute("delete from employee where empid=?",(empid,))
        cont.commit()
    elif choice==5:
        print("Existing!!!!")
        break
    else:
        print("Invaild choice")
