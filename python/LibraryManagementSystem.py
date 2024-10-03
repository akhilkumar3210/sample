user=[{'id':100, 'name': 'akhil', 'email': 'ak24152@gmail.com', 'mobno': 84743846346, 'password': 'akhil'}]
book=[]
while True :
    print(''' 
          1.Register
          2.Login
          3.Exit  
            ''')
    choice=int(input("Enter a Choice(1/2/3) : "))
    if choice == 1:
        if len(user)==0:
            id=100
        else:
            id=user[-1]['id']+1
            print(id)
            name=input("Enter  Name : ")
            email=input("Enter  Email ID :")
            mobno=int(input("Enter Mobile No : "))
            password=input("Enter Password : ")
            user.append({'id':id,'name':name,'email':email,'mobno':mobno,'password':password})
            # print(user)
    elif choice == 2:
        username=input("Enter UserName :")
        password=input("Enter Password : ")
        f=0
        if username=='admin' and password=='admin':
            print("Admin Login!!!")
            f=1
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
                    if len(book)==0:
                            id=100
                    else:
                        id=book[-1]['id']+1
                        print(id)
                    name=input("Enter  Name : ")
                    stock=input("Enter  stock :")
                    price=int(input("Enter price : "))
                    book.append({'id':id,'name':name,'stock':stock,'price':price})
                    # print(book)
                elif choice==2:
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
                elif choice ==3:
                    id=int(input("Enter ID : "))
                    f1=0
                    for i in book:
                        if i['id']==id:
                            f1=1
                            book.remove(i)
                    if f1==0:
                        print("Book Is Not Available")
                elif choice==4:
                    print('{:<8}{:<20}{:<30}{:<15}'.format('name','Stock ','Price'))
                    print('_'*100)
                    for i in book:
                        print('{:<8}{:<20}{:<30}{:<15}'.format(i['name'],i['stock'],i['price']))
                elif choice==5:
                    print('{:<8}{:<20}{:<30}{:<15}'.format('ID','Name','Email ID','Mobno'))
                    print('_'*100)
                    for i in user:
                        print('{:<8}{:<20}{:<30}{:<15}'.format(i['id'],i['name'],i['email'],i['mobno']))
                elif choice ==6:
                    print("Existing>>>>>>>>>>")
                    break

        if username.isdigit():
            username=int(username)
            for i in user:
                if i['id']==username and i['password']==password:
                    print("User Login!!!!")
                    f=2
            if f==0:
                print("Invaild Username Or Password !#$")
    elif choice == 3:
        print("Existing>.....")
        break
    else:
        print("Invaild Choice!!!!!!!!!!!!!")