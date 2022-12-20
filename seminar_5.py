# with open('task.txt', 'w') as data:
#     data.writelines('1 2 3 4 5 8 15 23 28')
# path = 'task.txt'
# f = open(path, 'r')
# data = f.read() + ''
# f.close()
#
# numbers = []
# while data != '':
#     space_pos = data.index('')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
#
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)

# другой способ с применением выражений и лямбда
# def select(f, col):
#     return [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# print(res) #получаем список чисел из файла
# res = where(lambda x: not x % 2, res)
# print(res) #получаем список четных чисел
# res = select(lambda x: (x, x**2), res)
# print(res)

# функция map

# li = [x for x in range(1,20)]
# print(li)
# li = list(map(lambda x: x + 10, li))
# print(li)

# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)


# def ispositive(x):
#     return x > 0

# фильтр
sp = [1, -5, 3, -7, 8]
res = list(filter(lambda s: s > 0, sp))
# print(res)

# сортировка
sp = [['e', 123], ['c', 1], ['d', 3], ['b', 56], ['a', 123]]
sp.sort(key=lambda x: (- x[1], x[0]))


# print(sp)


# 1.В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Входные данные	Выходные данные
# 1 2 3 5 6 7 8 	4

# path = 'file_task2.txt'
# data = open(path, 'r')
# a = data.read().split()
# print(a)  # вышел строчный список
# a = list(map(int, a))  # преобраз. в int
# print(a)
#
# data.close()
#
# for i in range(1, len(a)):
#    if a[i] != a[i-1] + 1:
#     print(a[i-1]+1)


#
# 2.	Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет, можно ли из этих отрезков составить треугольник.
# Входные данные	Выходные данные
# triangle(1, 1, 2)	Это не треугольник
# triangle(7, 6, 10)
# 	Это треугольник

# a = 6
# b = 3
# c = 4
#
# def triagle(a, b, c):
#     if a + b > c and b + c > a and a + b > c:
#         return True
#     return False
# print(triagle(a, b, c))
#


# 3.	Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

# res = list(map(lambda  x: x ** 2, filter(lambda x: x % 9 == 0, range(10, 100))))
# print(res)
# print(sum(res))
#


# 4.	Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся
# чисел в одну строчку через пробел.
#  пример  - 8 11 0 -23 140 1 => 11 -23
#
# sp = [- 8, 11, 0, -23, 140, 1]
#
# res = list(filter(lambda x: 10 < abs(x) < 100, sp))   # модуль abs отрицательное число переводит в положительное
# print(res)




# 5.	Дан список, вывести отдельно буквы и цифры.
# a = ( ‘1’, "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

# sp = ['1', "a", 'b', '2', '3', 'c']
#
# c = list(filter(lambda x: x.isdigit(), sp))
# print(c)
#
# b = list(filter(lambda x: x.isalpha(), sp))
# print(b)

# 6.  Предположим вы переписываете у друга рецепты в блокнот, но вам не нравится лук. Переписывайте без него.
# Формат ввода
# На первой строке вводится натуральное число N - количество пунктов рецепта:
# Далее следуют N строк - пункты рецепта.
#
# Формат вывода
# Одна строка - пункты рецепта, разделенные запятой и пробелом, без пунктов с упоминанием лука
#
#Ввод
# 5
# лук 1 головка
# картофелин штук 6
# картошку почистить
# лук порезать кольцами
# зажарить всё

# Вывод
# картофелин штук 6, картошку почистить, зажарить всё

# n = 5
# sp = []
# for i in range(n):
#     sp.append(input())
# print(sp)

# sp = ['лук 1 головка', 'картофелин штук 6', 'картошку почистить', 'лук порезать кольцами', 'зажарить всё']
#
# sp = list(filter(lambda x: 'лук' not in x, sp))
# print(*sp, sep=',')
# print(','.join(sp))
#
# sp.sort(key= lambda x: len(x))
# print(sp)



