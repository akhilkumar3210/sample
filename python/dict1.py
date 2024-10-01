a=int(input("Enter a Number : "))
d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
n=0
value=''
while a > 0:
    n=a%10
    a//=10
    demo=d[n]
    value=demo+value
print(value)

