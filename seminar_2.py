#  1. Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны).
# Входные данные	Выходные данные
# 10                   2
# 5
# 10
# a = int(input('Введите число А: '))
# b = int(input('Введите число В: '))
# c = int(input('Введите число С: '))
#
# if a == b == c:
#     print('Все числа совпадают')
# elif (a == b or b == c or a == c):
#     print('2')
# else:
#     print('0')



# 2. Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. В этой задаче можно обойтись без инструкции if.
# Входные данные	Выходные данные
# 7                 7 5 3 1
# 1
# print('Введите числа а и b, чтобы а > b')
# a = int(input('A: '))
# b = int(input('B: '))
# # for a in range (a,b,-2):
# #     a -= (a - 1) % 2
# #     print(a)
#
# # или
# for a in range (a - (a - 1) % 2, b - 1,-2):
#     print(a)

# или
#
# print('Введите числа а и b, чтобы а > b')
# a = int(input('A: '))
# b = int(input('B: '))
# while a >= b:
#     a -= (a - 1) % 2
#     print(a)
#     a -= 2


# 3. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# # Для N = 5: 1, -3, 9, -27, 81
# n = int(input('N: '))
# for i in range(n):
#     print((-3) ** i, end=" ")


# 4. Напишите программу, которая проверяет пятизначное число на палиндром.

# n = input('Введите число ')
# count = 0
# #
# for i in range(len(n) // 2):
#     if n[i] == n[-i - 1]:
#         count +=1
#
# if count == len(n) // 2:
#     print('Палиндром')
# else:
#     print('не палиндром')

#  или
# n1 = input('Введите число ')
# n2 = n1[:: -1]
# if n2 == n1:
#     print('Падиндром')
# else:
#     print('Не палиндром')


# 5. Удалить вторую цифру трёхзначного числа.

# n = int(input('Введите трехзначное число: '))
#
# print(n//100, n%10, sep="")

# n = input('Введите трехзначное число: ')
# print(n[0]+n[-1])


# 6. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
# n1 = 'jjmfjlnjj'
# n2 = 'jj'
# print(n1.count(n2))

# или
# n1 = 'jjmfjlnjj'
# n2 = 'jj'
#
# i = 0
# count = 0
# while i < len(n1):
#     if n1[i:i + len(n2)] == n2:
#         count += 1
#         i += (len(n2)-1)
#     i += 1
# print(count)
# Дополнительные задачи:
# 1. По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
# Входные данные	Выходные данные
# 50	             1
#                    4
#                    9
#                    16
#                    25
#                    36
#                    49
#
n = int(input('Введите число N: '))
# for i in range(1, n):
#     if i ** 2 < n:
#         print(i ** 2)
#     else:
#         break

res = [i for i in range(1, n) if i ** 2 < n]
print(res)

# 2.	Определите среднее значение всех элементов последовательности, завершающейся числом 0.
# Входные данные	Выходные данные
# 1               	5.666666666666667
# 7
# 9
# 0
#

# print('Введите числа, в конце 0')
# n = None
# sum = 0
# count = 0
# while n != 0:
#     n = int(input())
#     count += 1
#     sum += n
#
# count -= 1
# print(round(sum/count, 2))

# # или
# print('Введите числа, в конце 0')
# n = None
# sp = []
# while n != 0:
#     n = int(input())
#     sp.append(n)
# print(round(sum(sp)/(len(sp)-1), 2))