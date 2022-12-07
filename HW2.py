# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:
# # - 6782 -> 23
# # - 0,56 -> 11
#
#
# a = input("Введите число: ")
# s = 0
# for i in a:
#     if i.isdigit(): # если i является числом, то его суммируем
#         s += int(i)
# print(s)
#
#
#
#
# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# # Пример:
#
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#
# N = int(input('Введите число n: '))
# sp = []
# number = 1
#
# for i in range(N):
#     i += 1
#     number *= i
#     sp.append(number)
# print(sp, end=",")
#
# # или такой способ
#
# n = int(input('Введите число  '))
# p = 1
# for i in range(1, n + 1):
#     p = p * i
#     print(p, end=' ')
#
# exit()
#
# # Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#
# N = int(input('Введите число n: '))
# sp = list()
#
# for i in range(1, N):
#     sp.append(i)
# print(sp)
#
# s = 0
# for i in sp:
#     s += (1 + 1 / i) ** i
# print(round(s, 2))


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных
# позициях. Позиции хранятся в файле file.txt в одной строке одно число.


data = open('file.txt', 'w')
data.write('1\n')
data.write('2\n')
data.close()

N = int(input('Введите число n: '))
sp = list()

for i in range(-N, N+1):
    sp.append(i)
print(sp)

with open('file.txt', 'r') as f:
    index = f.readlines()
mul = 1
for i in index:
    mul *= sp[int(i)]
print(mul)



# Реализуйте алгоритм перемешивания списка(shuffle использовать нельзя, другие методы из библиотеки random - можно).

import random
N = int(input('Введите число n: '))
sp = list()

for i in range(N):
    sp.append(i)
print(sp)

sp2 = sp[:]
sp_len = len(sp)
for i in range(sp_len):
    index_x = random.randint(0, sp_len-1)
    tmp = sp2[i]
    sp2[i] = sp2[index_x]
    sp2[index_x] = tmp
print(sp2)

