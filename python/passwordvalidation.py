import re
a=input("Enter a Password : ")
print(re.search('[a-z].{7}[A-Z].{1}',a))