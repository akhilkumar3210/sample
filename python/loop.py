# for i in range(10):
    # print(i)
# for i  in range(6,0,-1):
    # print("*"*i)
n=int(input("ENTER A NUMER :"))
r=0
while n != 0:
    digit = n % 10
    r = r * 10 + digit
    n //= 10
print("Rev No :",str(r))