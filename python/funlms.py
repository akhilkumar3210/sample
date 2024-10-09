user=[]
book=[]

def register():
    if len(user)==0:
            id=100
    else:
            id=user[-1]['id']+1
    print(id)
    name=input("Enter  Name : ")
    email=input("Enter  Email ID :")
    mobno=int(input("Enter Mobile No : "))
    password=input("Enter Password : ")
    user.append({'id':id,'name':name,'email':email,'mobno':mobno,'password':password,'book':[]})
def login():
    username=input("Enter UserName :")
    password=input("Enter Password : ")
    f=0
    users=''
    if username=='admin' and password=='admin':
        f=1
    if username.isdigit():
        username=int(username)
        for i in user:
            if i['id']==username and i['password']==password:
                f=2
                users=i
    if f==0:
        print("Invaild username and password")
    return f,users
def addbook():
    if len(book)==0:
        id=1000
    else:
        id=book[-1]['id']+1
    print(id)
    name=input("Enter  Name : ")
    stock=int(input("Enter  stock :"))
    price=int(input("Enter price : "))
    book.append({'id':id,'name':name,'stock':stock,'price':price})
def updatebook():
    id=int(input("Enter ID : "))
    f1=0
    for i in book:
        if i['id']==id:
            f1=1
        i['name']=input("Enter New Name : ")
        i['stock']=input("Enter New Stock : ")
        i['price']=input("Enter New Price : ")
        if f1==0:
            print("Book Is Not Available")
def deletebook():
    id=int(input("Enter ID : "))
    f1=0
    for i in book:
        if i['id']==id:
            f1=1
            book.remove(i)
        if f1==0:
            print("Book Is Not Available")
def viewbook():
    print('{:<10}{:<20}{:<30}{:40}'.format('Id','name','Stock ','Price'))
    print('_'*100)
    for i in book:
        print('{:<10}{:<20}{:<30}{:<40}'.format(i['id'],i['name'],i['stock'],i['price']))
def viewuser():
    print('{:<8}{:<20}{:<30}{:<15}'.format('ID','Name','Email ID','Mobno'))
    print('_'*100)
    for i in user:
        print('{:<8}{:<20}{:<30}{:<15}'.format(i['id'],i['name'],i['email'],i['mobno']))
def viewpro(users):
    print(users)
def lendbook():
    id=int(input("Enter a ID : "))
    f1=0
    for j in book:
        if j['id']==id:
            f1=1
        if  j['stock']>0:
            users['book'].append(id)
            j['stock']-=1
        else:
            print("Out Of Stock")
    if f1==0:
        print("Book is not Avilable")
def returnbook():
    id=int(input("Enter a Id : "))
    f1=0
    for j in book:
        if j['id']==id and id in users['book']:
            f1=1
            j['stock']+=1
            users['book'].remove(id)
    if f1==0:
        print("Book Is Not Avilable")
def bookhand():
    if len(users['book'])==0:
        print("No Books")
    else:
        print(users['book'])
while True:
    print(''' 
          1.Register
          2.Login
          3.Exit  
            ''')
    choice=int(input("Enter a Choice(1/2/3) : "))
    if choice == 1:
            register()
    elif choice==2:
            f,users=login()
            if f==1:
                    while True:
                        print(''' 
                                        1.Add Book
                                        2.Update Book
                                        3.Delete Book
                                        4.View Book
                                        5.View Users
                                        6.Logout
                                                    ''')
                        choice=int(input("Enter a Choice(1/2/3/4/5/6) : "))
                        if choice == 1:
                            addbook()
                        elif choice ==2:
                            updatebook()
                        elif choice==3:
                            deletebook()
                        elif choice==4:
                            viewbook()
                        elif choice==5:
                            user=viewuser()
                        elif choice==6:
                            print("Logout!!!!")
                            break
            elif f==2:
                while True:
                        print('''
                               1.view profile
                               2.View Books
                               3.Lend Books
                               4.Return Books
                               5.Books In Hands
                               6.Logout!!!     
                                        ''')
                        choice=int(input("Enter a Choice(1/2/3/4/5) : "))
                        if choice== 1:
                           viewpro(users)
                        elif choice== 2:
                            viewbook()
                        elif choice ==3:
                           lendbook()
                        elif choice ==4:
                            returnbook()
                        elif choice==5:
                            bookhand()
                        elif choice==6:
                            print("Logout!!!!!!")
                            break
                        
            else:
                ("Invaild")