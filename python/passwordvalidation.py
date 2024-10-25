import re
a=input("Enter a Password : ")
print(re.search('^[A-Z].{1}.*[a-z].{7}',a))