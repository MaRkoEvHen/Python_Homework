import keyword
import string

while True:
    get_variable = input("Please enter a variable name: ")
    forbidden_symbol= string.punctuation.replace("_", "") + " "
    if get_variable == "exit" or get_variable == "quit":
        print(f"Exiting the program.")
        break
    if not get_variable:
        print("False")
        continue
    if get_variable in keyword.kwlist:
        print(f"'{get_variable}' False")
        continue
    if get_variable[0] in string.digits:
        print(f"'{get_variable}' False")
        continue
    if "__" in get_variable or " " in get_variable:
        print(f"'{get_variable}' False")
        continue
    for char in get_variable:
        if char in forbidden_symbol or char.isupper():
            print(f"'{get_variable}' False")
            break
    else:
        print(f"'{get_variable}' True")



