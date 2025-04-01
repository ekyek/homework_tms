# print("Hello World")
# print("It is my first python program")
# print("And it is the end of my program")
# print("Bye-bye")


# print("первая строка\nвторая строка\nтретья строка")
# print("первая строка","вторая строка","третья строка", sep="\n")
# print("первая строка","вторая строка","третья строка", sep="\t")

# name="Лиза"
# print(f"Привет, {name}")
# print("Привет,", name)

# age=22
# print(f"мой возраст = {age}")
# age=age+5
# # age += 5 
# print(f"мой возраст через 5 лет = {age}")


#1

import math
a = 10
b = 15
x = 20
y1 = a**2 / 3 + (a**2 + 4) / b + (math.sqrt(a**2 + 4)) / 4 + (math.sqrt((a**2 + 4)**3)) / 4
print('a) y =', y1)

y2 = math.cos(x) + math.sin(x)
print('b) y =', y2)

y3 = ((math.cos(x ** 2))**2 + (math.sin(2 * x - 1))**2) ** (1/3)
print('c) y =', y3)

y4 = 5 * x + 3 * x**2 * math.sqrt(1 + (math.sin(x))**2)
print('d) y =', y4)

#2

i = float(input("Введите годовую процентную ставку"))
s = float(input("Введите сумму займа"))
n = int(input("Введите кол-во месяцев, на которое взят кредит"))
p = i / 12

m = (s * p * ((1 + p)**n)) / ((1 + p)**n - 1)
print("Ежемесячная выплата составит:", m)

#3

R_1 = float(input("Введите радиус орбиты планеты № 1 в млн.км"))
v_1 = float(input("Введите орбитральную скорость планеты № 1 в км/ч"))

L_1 = (2 * R_1 * math.pi) / v_1

R_2 = float(input("Введите радиус орбиты планеты № 2 в млн.км"))
v_2 = float(input("Введите орбитральную скорость планеты № 2 в км/ч"))

L_2 = (2 * R_2 * math.pi) / v_2

print("Длина года на планете № 1 =", L_1)
print("Длина года на планете № 2 =", L_2)

if L_1 > L_2:
    print("Правда")
else:
    print("Неправда")

