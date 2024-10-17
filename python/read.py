# f=open('demo1','r')
# a=f.read(10)
# print(a)
# print('_'*25)
# f.seek(0)
# b=f.read()
# print(b)

# a=f.readline(2)
# print(a)
# b=f.readline()
# print(b)
# c=f.readline()
# print(c)

# a=f.readlines()
# print(len(a))

# a=f.read()
# print(len(a))

# a=f.readlines()
# print(a)
# f.seek(0)
# l=0
# u=0
# w=0
# lg=''
# for i in range(len(a)):
#     b=f.readline().strip()
#     c=b.split(' ')
#     # print(c)
#     for j in c:
#         if j!='':
#             w+=1
#             if len(j)>len(lg):
#                 lg=j
#     for j in b:
#         if j!=' ':
#             l+=1
#             if j.isupper():
#                u+=1
# print(l)
# print(u)
# print(l-u)
# print(w)
# print(lg)

import os
# if os.path.exists('demo2'):
#     os.remove('demo2')
# else:
#     print('File Doesnt Exit')

# os.mkdir("Sample")
# os.rmdir("Sample")