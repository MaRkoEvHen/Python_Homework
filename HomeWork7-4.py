

def common_elements():

    list_first = [el for el in range(0,101) if el % 3 == 0 ]
    list_second = [el for el in range(0,101) if el % 5 == 0 ]

    set_first = set(list_first)
    set_second = set(list_second)

    result = set_first.intersection(set_second)
    return result


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")