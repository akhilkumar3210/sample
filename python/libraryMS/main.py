import reg
while True:
    print(''' 
          1.Register
          2.Login
          3.Exit
            ''')
    choice=int(input("Enter a choice : "))
    if choice == 1:
        reg.reg()
    elif choice == 2:
        reg.login()
        f,users=reg.login()
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
                else:
                    print("Invalid")