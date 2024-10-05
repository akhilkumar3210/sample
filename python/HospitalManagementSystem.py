patient=[]
administration=[]
while True:
    print('''
            1.Register
            2.Doctor Details
            3.Administration 
            4.Patient Details
            5.Signout    
                        ''')
    choice=int(input("Enter a Choice(1/2/3)  : "))
    if choice==1:
        if len(patient)==0:
            id=1
        else:
             id=patient[-1]['id']+1
             print(id)
        date=str(input("Enter Date Of Booking : "))
        name=input("Enter a Name : ")
        age=int(input("Enter Your Age : "))
        gender=input("Enter your Gender : ")
        phno=int(input("Enter Your Mobile No : "))
        patient.append({'id':id,'date':date,'name':name,'age':age,'gender':gender,'phno':phno})
        # print(patient)
    elif choice ==2:
        print('{:<10}{:<20}{:<30}{:40}'.format('name','Gender','specialist','phnum'))
        print('_'*100)
        for i in administration:
            print('{:<10}{:<20}{:<30}{:<40}'.format(i['name'],i['gen'],i['specialist'],i['phnum']))
    elif choice == 3:
        username=input("Enter UserName :")
        password=input("Enter Password : ")
        f=0
        if username=='admin' and password=='admin':
                print("Administration Login Successfully!!")
                f=1
                while True:
                    print(''' 
                    1.Display details
                    2.Add a new members
                    3.Delete Members
                    4.Make An Exit         
                            ''')
                    choice=int(input("Enter a Choice(1/2/3/4) : "))
                    if choice ==1:
                        print('{:<10}{:<20}{:<30}{:40}'.format('Id','Date','name','Age','Gender','phno'))
                        print('_'*100)
                        for i in patient:
                            print('{:<10}{:<20}{:<30}{:<40}'.format(i['id'],i['date'],i['name'],i['age'],i['gender'],i['phno']))
                    elif choice ==2:
                         while True:
                            print('''
                                    1.Enter Docter Details
                                    2.Update Doctor Details
                                    3.View Doctor Details
                                    4.Exit     
                                                ''')
                            choice=int(input("Enter a Choice(1/2/3) :"))
                            if choice==1:
                                if len(administration)==0:
                                    id=1000
                                else:
                                    id=administration[-1]['id']+1
                                print(id)
                                name=input("Enter a name :")
                                age=int(input("Enter your Age :"))
                                specialist=input("Enter your specialist-in : ")
                                gen=input("Enter your Gender : ")
                                address=input("Enter your Address :")
                                phnum=int(input("Enter your phno :"))
                                administration.append({'id':id,'name':name,'age':age,'specialist':specialist,'gen':gen,'address':address,'phnum':phnum})
                            elif choice ==2:
                                id=int(input("Enter ID : "))
                                f1=0
                                for i in administration:
                                    if i['id']==id:
                                        f1=1
                                    i['name']=input("Enter New Name : ")
                                    i['age']=int(input("Enter New Age : "))
                                    i['specialist']=input("Enter New specailist-in : ")
                                    i['gen']=input("Enter New age : ")
                                    i['address']=input("Enter a New Address : ")
                                    i['phnum']=int(input("Enter New phno : "))
                                if f1==0:
                                    print("Doctor Is Not Available")
                            elif choice ==3:
                                print('{:<10}{:<20}{:<30}{:40}'.format('name','Gender','specialist','phnum'))
                                print('_'*100)
                                for i in administration:
                                    print('{:<10}{:<20}{:<30}{:<40}'.format(i['name'],i['gen'],i['specialist'],i['phnum'])) 
                            elif choice ==4 :
                                print("Exit........")
                                break
                    elif choice ==3:
                        id=int(input("Enter ID : "))
                        f1=0
                        for i in administration:
                            if i['id']==id:
                                f1=1
                                administration.remove(i)
                        if f1==0:
                            print("Doctor Is Not Available")
                    elif choice==4:
                        print("Exit.......")
                        break
    elif choice==4:
        while True:
            print(''' 
                    1.Show Patient Info
                    2.Add New Patient
                    3.Discharge Summary
                    4.Exit
                            ''')
            choice=int(input("Enter a Choice : "))
            if choice == 1:
                print('{:<10}{:<20}{:<30}{:40}'.format('Id','Date','name','Age','Gender','phno'))
                print('_'*100)
                for i in patient:
                    print('{:<10}{:<20}{:<30}{:<40}'.format(i['id'],i['date'],i['name'],i['age'],i['gender']))
            elif choice==2:
                print
    elif choice==5:
        print("SignOut.........")
        break