l=[]
limit=int(input("Enter a Limit : "))
for i in range(limit):
    name=input("Enter a Name : ")
    age=int(input("Enter a Age : "))
    l.append({'name':name,'age':age})
print(l)