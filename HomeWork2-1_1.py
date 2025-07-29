get_number = int(input("Введіть 4-х значне число:"))
num1= get_number//1000
num2= (get_number%1000)//100
num3= (get_number%100)//10
num4= get_number%10
print(num1)
print(num2)
print(num3)
print(num4)

print(f"{num1}\n{num2}\n{num3}\n{num4}") #Вивід через f-строку. Вирішив почитати документацію#
