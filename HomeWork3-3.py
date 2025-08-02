my_list=[]
first_list=[]
second_list=[]
length_list = len(my_list)
dividing_point = length_list//2

if length_list == 0:
    first_list = []
    second_list = []
elif length_list % 2==0 :
    first_list = my_list[0:dividing_point]
    second_list= my_list[dividing_point:]
elif length_list % 2 != 0:
    first_list = my_list[0:dividing_point +1]
    second_list = my_list[dividing_point +1 :]


new_list = [first_list, second_list]

print(new_list)

