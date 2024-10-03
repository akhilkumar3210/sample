l=[]
while True:
    print('''
          1.Add Student Details
          2.View Student Details
          3.Update Student Details
          4.Delete Student Details
          5.Existing!!!
          ''')
    choice = int(input("Enter a Choice(1/2/3/4/5) : "))
    if choice == 1:
        roll_no=int(input('Roll_no :'))
        name=str(input("Name :"))
        email=str(input("Email ID :"))
        course=str(input("Course :"))
        l.append({'roll_no':roll_no,'name':name,'email':email,'course':course})
    elif choice ==2:
        print('{:<8}{:<20}{:<30}{:<15}'.format('Roll_no','Name','Email ID','Course'))
        print('_'*100)
        for i in l:
            print('{:<8}{:<20}{:<30}{:<15}'.format(i['roll_no'],i['name'],i['email'],i['course']))
        # print(l)
    elif choice == 3:
        roll_no=int(input("Enter a Rollno : "))
        f=0
        for i in l:
            if i['roll_no']==roll_no:
                name=str(input('name : '))
                i['name']=name
                f=1
        if f==0:
            print('id not avilable')
    elif choice == 4:
        roll_no=int(input("Enter a Rollno : "))
        f=0 
        for i in l:
            if i['roll_no']==roll_no:
                l.remove(i)
                f=1
        if f==0:
            print(" Not a valid RollNo")
    elif choice == 5:
        print("Existing!!!!!!!!!!!!!!!")
        break
        
    else:
        print(" Invaild Choice")
