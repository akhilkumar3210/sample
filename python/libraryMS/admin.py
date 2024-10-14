book=[]
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
