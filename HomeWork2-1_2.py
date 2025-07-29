get_number =int(input("Введіть 5-ти значне число: "))
num1=get_number%10
num2=(get_number%100)//10
num3=(get_number%1000)//100
num4=(get_number%10000)//1000
num5=get_number//10000
print(f"{num1}{num2}{num3}{num4}{num5}")