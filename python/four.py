while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter your choice(1/2/3/4/5)"))
    if choice == 1:
        a=int(input("Enter a 1st no:"))
        b=int(input("Enter a 2nd no:"))
        sum1=a+b
        print("Addition:",sum1)
    elif choice == 2:
        a=int(input("Enter a 1st no:"))
        b=int(input("Enter a 2nd no:"))
        sum2=a-b
        print("Subtraction",sum2)
    elif choice == 3:
        a=int(input("Enter a 1st no:"))
        b=int(input("Enter a 2nd no:"))
        sum3=a*b
        print("Multiplication",sum3)
    elif choice == 4:
        a=int(input("Enter a 1st no:"))
        b=int(input("Enter a 2nd no:"))
        sum4=a/b
        print("Division",sum4)
    elif choice == 5:
        print("Exiting....")
        break
    else:
        print("Wrong")


