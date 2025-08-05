my_list=[0, 1, 0, 12, 3]
zero_list=[]
new_list=[]
for el in my_list:
    if el == 0 :
        zero_list.append(el)
    elif el < 0:
        new_list.append(el)
    elif el > 0:
        new_list.append(el)
my_list = new_list + zero_list
print(my_list)






