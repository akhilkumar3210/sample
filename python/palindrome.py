# def is_palindrome(String):
    # String=String.lower()
    # left,right = 0,len(String) -1
    # while left < right :
    #     if String[left] != String[right]:
    #         return False
    #     left += 1
    #     right -= 1
    #     return True
n=int(input("ENTER A NUMER :"))
r=0
a=n
while n != 0:
    digit = n%10
    r = r * 10 + digit
    n //= 10
print("Rev No :",str(r))
if r==a:
    print(" palindrome")
else:
    print(" Not a palindrome")