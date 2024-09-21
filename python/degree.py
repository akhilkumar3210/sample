print("1.Celsius To Fahrenheit")
print("2.Fahrenheit To Celsius")
print("3.Celsius To Kelvin")
print("4.Fahreheit To Kelvin")
print("5.kelvin To Celsius")
print("6.Kelvin To Fahrenheit")
choice=int(input("Enter Your Choice :"))
if(choice == 1):
    a=float(input("Enter a temperature in celsius :"))
    f=(a*9/5)+32
    print("Temperature in Fahreheit :",f)
elif(choice == 2):
    a=float(input("Enter Temperature in Fahrehiet :"))
    c= (a-32)*5/9
    print("Temperature in Celsius",c)
elif(choice == 3):
    a=float(input("Enter celsius :"))
    k=a+273.15
    print("Temperature in kelvin :",k)
elif(choice == 4):
    a=float(input("Enter Temperature in Fahrehiet :"))
    k=(5/9)*(a-32)+273.15
    print("Temperature in kelvin",k)
elif(choice == 5):
    a=float(input("Enter Temperature in kelvin :"))
    c=a-273.15
    print("Temperature in Celsius :",c)
elif(choice == 6):
    a=float(input("Enter Temperature in kelvin:"))
    f=(a-273.15)*9/5+32
    print("Temperature in Fahreheit : ",f)
else:
    print("Wrong")