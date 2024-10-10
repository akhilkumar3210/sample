# def add(a,b):
#     print(a+b)
# print(add(13,87))

# add=lambda a,b,c,d:a+b+c+d
# print(add(29,85,99,7))
# l=[1,2,3,4,5,6,7,8,]
# a=[]
# for i in l:
#     a.append(i**3)
# print(a)
# a=map(lambda i:i**3,l)
# print(list(a))
# print(list(map(lambda i:i**3,l)))
# def sample(i):
#     return i**3
# print(list(map(sample,l)))
# a=filter(lambda i:i%2==0,l)
# print(list(a))
# def even(i):
#     return i%2==0
# print(list(filter(even,l)))
# def odd(i):
#     return i%2==1
# print(list(filter(odd,l)))

# l=['pineapple','spoon','mesh','ring','bulb']
# a=input("Enter a Alphabet : ")
# for i in l:
#     if a in i:
#         print(i)
# b=filter(lambda i:a in i,l)
# print(list(b))
# print(list(filter (lambda i: a in i,l)))
# l=[2,1,3,4,9,7,8,3,4,6,7]
# a=[ i**3 for i in l]
# print(a)
# l=[2,1,3,4,9,7,8,3,4,6,7]
# a=[ i for i in l if i%2==0]
# print(a)
l=['apple','mango','kiwi','grapes','pineapple']
s=''
# b=[ i for i in l if len(i)]
for i in l:
    if len(i)>len(s):
        s=i
print(i)


