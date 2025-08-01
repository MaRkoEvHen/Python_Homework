my_list = [1,2,3,4,5,6,7,8,9]
if len(my_list) <= 1:
    print(f"Ми його не змінюємо {my_list}")
else:
    a = my_list[-1]
    del my_list[-1]
    my_list.insert(0, a)
    print(my_list)



