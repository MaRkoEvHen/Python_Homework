import random
my_list=[]
new_list=[]
list_length = random.randint(3, 10)
for el in range(list_length):
    my_list.append(random.randint(3,10))
new_list=[my_list[0],my_list[2],my_list[-2]]
print(my_list) #Вивід згенерованого нового списку
print(new_list) #Вивід нового списку з 3-ма елементами