# l=[1,2,3,5,2,4,1,3,8,9,7,5,4]
# s=set(l)
# l=list(s)
# print(l)
l=[1,2,[10,{5,6}],4]
l[2][1].add(12)
print(l)