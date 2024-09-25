my_list =[5,4,7,2]
target=9
for i in range(len(my_list)):
    for k in range(len(my_list)):
        t=my_list[i]+my_list[k]
        if t==target:
            print(i,k)
    
        
    