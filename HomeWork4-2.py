my_list=[0,1,7,2,4,8]
# my_list=[]
new_list=[]
if len(my_list) == 0: #Перевірка чи пустий масив
    print(0)
else:
    for ind,el in  enumerate(my_list):
        if ind%2==0:               #Перевірка на парність індексів
            new_list.append(el)    #Додаємо в новий масив ці числа
    sum_element=sum(new_list)
    last_element=my_list[-1]
    result = sum_element*last_element
    print(result)



