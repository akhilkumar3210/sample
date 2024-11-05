pb=int(input("Enter price of bike : "))
tax=0
if pb<=50000:
    tax=pb*5/100
    print("Tax : ",tax)
elif pb>50000 and pb<=100000:
    tax=pb*10/100
    print("Tax :",tax)
elif pb>100000:
    tax=pb*15/100
    print("Tax : ",tax)
else:
    print('no ')