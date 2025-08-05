my_list=[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0,-1]
zero_list=[]
new_list=[]
for el in my_list:
    if el == 0 :
        zero_list.append(el)
    elif el < 0:
        new_list.append(el)
    elif el > 0:
        new_list.append(el)
new_list.sort()
my_list = new_list + zero_list
print(my_list)





