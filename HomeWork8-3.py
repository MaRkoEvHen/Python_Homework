def find_unique_value(some_list):

    unique_value=[el for el in some_list if some_list.count(el) == 1]
    if unique_value:
        return unique_value[0]
    return None

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
