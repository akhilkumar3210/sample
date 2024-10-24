import re

# a='hello World hello'
# print(re.sub('hello','Helllo',a,1))

# print(re.findall('hello',a))

# print(re.search('hello',a))
# print(re.search('h',a))
# print(re.search('z',a))

a='xyzdfahajkl54656ABC'
# print(re.search('ghajkl',a))
# print(re.search('[a-z]',a))
# print(re.search('[A-Z]',a))
# print(re.search('[A-z]',a))
# print(re.search('[abc]',a))
# print(re.search('a..',a))
# print(re.search('a.*',a))
# print(re.search('a.+',a))
# print(re.search('j.+',a))
# print(re.search('l.?',a))
# print(re.search('a.?',a))

# print(re.search('[a-z].*[A-Z]',a))
# print(re.search('[a-z].*[0-9].*[A-Z]',a))
# print(re.search('[a-m].*[0-9].*[A-Z]',a))
print(re.search('[a-m0-9A-Z]',a))

















