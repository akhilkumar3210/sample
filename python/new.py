# f=open('demo','a')
# f.write('Welcome To All ')
# f.write('Introduction')
# f.write('Vroooooooooooom')
# f.write('12345')
# f.write('[1,2,3,4,5]')
# f.write('Welcome To All')
# limit=int(input('Enter a Limit : '))
# f=open('demo','w')
# for i in range(limit):
#     name=input("Enter a Name :")
#     f.write(name+'\n')
a=int(input("Enter a Number : "))
f=open('demo','a')
for i in range(1,11):
    print(a,'x',i,'=',a*i)
    f.write(str(a)+'x'+str(i)+'='+str(a*i)+'\n')
    





























