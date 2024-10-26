import re

a=input("Enter a Mobile Number : ")

if len(a)==10 and a.isdigit() and re.search('[6-9].{9}',a):
    print("Valid...")
else:
    print("Invaild!!!")