get_number1 = input("Введіть число 1-ше число: ")
get_action = input("Введіть дію +,-,*,/,%,//,**: ")
get_number2 = input("Введіть число 2-ше число: ")

get_number1=int(get_number1)
get_number2=int(get_number2)


if get_number2 == 0 and get_action in ("/","//","%") : # перевірка ділення на нуль
    print ("На нуль ділити не можна")
elif get_action == "+":
    summ = get_number1 + get_number2
    print(f"{get_number1} + {get_number2} = {summ} ")
elif get_action == "-":
    minus = get_number1 - get_number2
    print(f"{get_number1} - {get_number2} = {minus} ")
elif get_action == "*":
    mnoj = get_number1 * get_number2
    print(f"{get_number1} * {get_number2} = {mnoj} ")
elif get_action == "/":
    dilFloat = get_number1 / get_number2
    print(f"{get_number1} / {get_number2} = {dilFloat} ")
elif get_action == "//"  :
    dilInt = get_number1 // get_number2
    print(f"{get_number1} // {get_number2} = {dilInt} ")
elif get_action == "%":
    chastka = get_number1 % get_number2
    print(f"{get_number1} % {get_number2} = {chastka} ")
elif get_action == "**":
    step = get_number1 ** get_number2
    print(f"{get_number1} ** {get_number2} = {step} ")
else:
    print("Ви ввели не правильну дію")



