# y = [int(i) for i in input().split()]   создание строки из набора чисел

# print(y)


# # Обращение к словарю
# access = {'login': 'ivan', 'password': '123'}
# login = input('Введите логин ')
# password = input('Введите пароль ')
# if login == access['login'] and password == access['password']:
#     print('Вход разрешен')
# else:
#     print('Вы ввели неверный логин и/или пароль')

#  Как наполнить словарь
# slovar = {}
# slovar['sity'] = 'Moskow'
# print(slovar)

# Как посчитать количество повторяющихся элементов в списке  и внести в  словарь
# sp = [1, 1, 2, 2, 2, 4]  # {1: 2, 2: 3, 4: 1}
# slovar = {} # создали словарь
# for el in sp:
#     if el not in slovar: # если элемента нет еще в словаре, пишем 1
#         slovar[el] = 1
#     else:
#         slovar[el] += 1  # иначе добавляем 1
# print(slovar)
# print(slovar.get(2))
# print(slovar.get(8)) # None
# print(slovar.get(8, 0)) # если None, возвращается 0

# можно этот код записать методом get
# sp = [1, 1, 2, 2, 2, 4]  # {1: 2, 2: 3, 4: 1}
# slovar = {}
# for el in sp:
#     slovar[el] = slovar.get(el, 0) + 1
# print(slovar)


# 1.	Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
#

# sp = [int(i) for i in input().split()]       # split - разделитель, по умолчанию пробел
# print('Макс', max(sp), 'Мин', min(sp))


# 2.	Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1.	с помощью математических формул нахождения корней квадратного уравнения
# 2.	с помощью дополнительных библиотек Python

# import math
#
# a, b, c = [int(i) for i in input('Введите значения A, B, C ').split()]
# d = b ** 2 - 4 * a * c
# if d > 0:
#     x1 = (-b - math.sqrt(d)) / (2 * a)
#     x2 = (-b + math.sqrt(d)) / (2 * a)
#     print(f'Корни уравнения: x1 = {x1} x2 = {x2}')
#
# elif d == 0:
#     x1 = -b / (2 * a)
#     print('Корень = ', x1)
# else:
#     print('Корней нет')

#
# 3.	Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# x = int(input('Введите первое число '))
# y = int(input('Введите второе число '))
#
# maximum = max(x, y)
# if maximum % x == 0 and maximum % y == 0:
#     print(maximum)
# else:
#     for count in range(2, min(x,y) + 1):
#         if (maximum * count) % x == 0 and (maximum * count) % y == 0:
#             print(maximum * count)
#             break

# Второй способ

# a = 10
# b = 15
# p = a * b
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
#
# nod = a + b
# nok = p // nod
# print(nok, nod)


#
# 4.	В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
# Входные данные	     Выходные данные
# one two one tho three	   0 0 1 0 0

# sp = ['one', 'two', 'one', 'tho', 'three']
# slovar = {}
# for el in sp:
#     slovar[el] = slovar.get(el, -1) + 1
#     print(slovar[el], end=' ')



# 5.	Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.
# Входные данные	Выходные данные
# 3
# Hello             Hi
# Bye               Goodbye
# List              Array
# Goodbye        	Bye

# slovar = {}
# slovar['Hello'] = 'Hi'
# slovar['Bye'] = 'Goodbye'
# slovar['List'] = 'Array'
# slovar['Goodbye'] = 'Bye'
#
# print(slovar)
#
# slovo = input('Введите слово ')
# for key, values in slovar.items():
#     if slovo == key:
#         print(values)
#     if slovo == values:
#         print(key)




# 6.	Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# Входные данные	Выходные данные
# 1
# apple orange banana banana orange	banana
#
sp = ['apple', 'orange', 'banana', 'banana', 'orange', 'banana']
slovar = {}
for el in sp:
    slovar[el] = slovar.get(el, 0) + 1
print(slovar, end=' ')
print()
slovar2 = dict(sorted(slovar.items()))  # сортировка по ключу в алфавитном порядке
print(slovar2)

maximum = max(slovar2.values())
print(maximum)

for key, value in slovar2.items(): # находим наибольшее значение, выводим его ключ
    if value == maximum:
        print(key)
