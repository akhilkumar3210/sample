import add,sub,mul,div
from number import num

while True:
    print(''' 
           1.Add
           2.Sub
           3.Mul
           4.Div
           5.Exit  
                ''')
    choice=int(input("Enter a Choice(1/2/3/4/5): "))
    if choice == 1:
        a,b=num()
        add.add(a,b)
    elif choice ==2:
        a,b=num()
        sub.sub(a,b)
    elif choice == 3:
        a,b=num()
        mul.mul(a,b)
    elif choice == 4:
        a,b=num()
        div.div(a,b)
    elif choice == 5:
        break
    else:
        print("Wrong Choice !!!!!!")