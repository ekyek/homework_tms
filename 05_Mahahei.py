print("№1a")
from math import factorial

x = int(input("Введите x >"))
result1 = 0 
for n in range(0,100):
    numinator1 = (-1)**n * x**(2*x+1)
    denominator1 = factorial(2*n+1)
    result1 += numinator1/denominator1
print(f"sin{x} ~= {result1}")

print("№1b")
from math import factorial

x = int(input("Введите x >"))
result2 = 0 
for n in range(0,100):
    numinator2 = (-1)**n * x**2*n
    denominator2 = factorial(2*n)
    result2 += numinator2/denominator2
print(f"cos{x} ~= {result2}")

# print("№2")

# N = int(input("введите стоимость телефона"))
# k = int(input("введите сколько можете откладывать"))
# saved_money = 0
# days = 0
# for i in range(0, N): #for i in range(0, int(N)):
#     while saved_money < N:
#     saved_money += k
#     days += 1
#     if saved_money >= N:
#         break
# print(f"потребуется {days} дней, чтобы накопить на телефон")

