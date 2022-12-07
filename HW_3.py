# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# o [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#
sp = [2, 3, 5, 9, 3]

summa = 0

for i in range(len(sp)):
    if i % 2 != 0:
        summa += sp[i]
print(summa)



#
# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# o [2, 3, 4, 5, 6] => [12, 15, 16];
#
# o [2, 3, 5, 6] => [12, 15]
#


from random import randint

num = int(input('Введите размер списка '))
sp = []
sp_mul = []

for i in range(num):
    sp.append(randint(0, 10))

print(sp)

for i in range((len(sp)+1) // 2):
    sp_mul.append(sp[i] * sp[-1 - i])

print(sp_mul)



# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#
sp = [1.1, 1.2, 3.1, 5, 10.01]
sp2 = []

for i in sp:
    x = i - int(i)
    x = round(x, 2)
    sp2.append(x)
print(sp2)

print(max(sp2) - min(sp2))



#
# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное (встроенными методами пользоваться нельзя).
#
# Пример:
#
# o 45 -> 101101
#
# o 3 -> 11
#
# o 2 -> 10

number = int(input('Введите десятичное число: '))
bi = ''
while number > 0:
    bi = str(number % 2) + bi
    number = number // 2
print(bi)

#
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# o для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = 9
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

sp = []

for e in range(1, 9):
    sp.append(fib(e))
print(sp)

for i in range(n):
    sp.insert(0, sp[1] - sp[0])
print(sp)
