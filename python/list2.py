l=[2,1,8,5,4,7,6,10,15,22,'a','b','c']
sum=0
for i in l:
    if type(i)==int or type(i)==float:
        sum+=i
        print(sum)