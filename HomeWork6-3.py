get_int = int(input("Enter a number: "))
while get_int > 9:
    prod = 1
    get_int_str = str(get_int)
    for get_char in get_int_str:
        digit = int(get_char)
        prod *= digit
    get_int = prod
print(f"Добуток: {get_int}")



