l=[1,2.5,'abc',6,9,6]
sum=0
for i in l:
    try:
        sum+=i
    except:
        pass
print(sum)
