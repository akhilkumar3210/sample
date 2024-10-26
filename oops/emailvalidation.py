import re

a=input("Enter ur Email Id : ")
if re.search('^[a-z].{2}.*@gmail.com$',a):
    print('Valid...')
else:
    print('Invaild!!!')