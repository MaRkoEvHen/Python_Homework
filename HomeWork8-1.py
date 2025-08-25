
def add_one(some_list):

    for el in range(len(some_list) -1, -1, -1):
        if some_list[el] < 9:
            some_list[el] += 1
            return some_list
        else:
            some_list[el] = 0
    some_list.insert(0, 1)
    return some_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
