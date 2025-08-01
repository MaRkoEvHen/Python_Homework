my_list = [1,2,3,4,5,6,7,8,9]
if len(type_list) <= 1:
    print(f"Ми його не змінюємо {type_list}")
else:
    a = type_list[-1]
    del type_list[-1]
    type_list.insert(0, a)
    print(type_list)



