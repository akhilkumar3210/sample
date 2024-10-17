limit=int(input("Enter a limit : "))
f=open('demo','w')
for i in range(1,11):
    for j in range(1,limit+1):
        print(i,'x',j,'=',i*j)
        f.write(str(i)+'x'+str(j)+'='+str(i*j)+'\n')
   