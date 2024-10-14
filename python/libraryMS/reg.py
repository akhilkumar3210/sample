user=[]
def reg():
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
    return user
    # print(user)
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