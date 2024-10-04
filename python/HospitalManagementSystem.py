import datetime

patient=[]
administration=[]
while True:
    print('''
            1.Register
            2.Administration
            3.Patient Details
            4.Signout    
                        ''')
    choice=int(input("Enter a Choice(1/2/3)  : "))
    if choice==1:
        if len(patient)==0:
            id=1
        else:
             id=patient[-1]['id']+1
             print(id)
        date=str(input("Enter Date Of Booking : "))
        date=datetime.datetime.now
        name=input("Enter a Name : ")
        dob=(input("Enter Your Date Of Birth : "))
        gender=input("Enter your Gender : ")
        phno=int(input("Enter Your MobileNo : "))
        patient.append({'id':id,'date':date,'name':name,'dob':dob,'gender':gender,'phno':phno})
        print(patient)
        
