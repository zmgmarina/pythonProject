# 1.	Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# Входные данные	Выходные данные
# 1 2 2 3 3 3	     1
#
list = [1, 2, 2, 3, 3, 3]

new_list = []
for i in list:
    if list.count(i) == 1:
        new_list.append(i)
print(*new_list) # * распаковывает (выводит из скобок) список

new_list = [i for i in list if list.count(i) == 1]
print(*new_list)

# 2.	Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# Входные данные	Выходные данные
# 1 5 2 4 3	         5 4

# list = [1, 5, 2, 4, 3]
# new_list = []
# for i in range(len(list) - 1):
#     if list[i] < list[i + 1]:
#         new_list.append(list[i + 1])
# print(*new_list)

# 3.	Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
#
# Подсказка: можно использовать модуль datetime

# import time
#
# print(time.time())
#
#
# def myrandom(n):
#     str_time = str(time.time())  # преобразуем число в строку
#     str_time = str_time.replace('.', '') # избавляемся от  точки
#     number = int(str_time) % n  # преобразуем в целое число и получаем остаток от деления
#     return number
#
#
# print(myrandom(1000))



# 4.	Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# Входные данные	Выходные данные
# 12
# Строка1
# Строка2
# Строка3
# Строка45
# Стр12ка	да

# number = 12
# list = []
# f = 0
# print('Введите элемент списка ')
#
# for i in range(5):            # заполняем список
#     list.append(input())
#
# for i in range(5):
#     if str(number) in list[i]:  # проверяем содержится ли в строке number
#         f = 1          # флажок(если встретился number, цикл заканчивается
#
# if f:
#     print('Да')
# else:
#     print('нет')

# Способ решения методом any (какой-нибудь содержит элемент содержит...)

# list = []
# print('Введите элемент списка ')
#
# for i in range(5):
#     list.append(input())
#
# if any('12' in el for el in list):
#     print('yes')
# else:
#     print('no')





#
# 5.	Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# •	список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# •	список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# •	список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# •	список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# •	список: [], ищем: "123", ответ: -1


# list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# element = "qwe"
# count = 0
#
# for i in range(len(list)):
#     if list[i] == element:
#         count += 1
#     if count == 2:
#         print(i)
#         break
# if count < 2:
#     print(-1)




# 3.	Вам дан английский текст. Закодируйте его с помощью азбуки Морзе:
# MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
#          'D': '-..', 'E': '.', 'F': '..-.',
#          'G': '--.', 'H': '....', 'I': '..',
#          'J': '.---', 'K': '-.-', 'L': '.-..',
#          'M': '--', 'N': '-.', 'O': '---',
#          'P': '.--.', 'Q': '--.-', 'R': '.-.',
#          'S': '...', 'T': '-', 'U': '..-',
#          'V': '...-', 'W': '.--', 'X': '-..-',
#          'Y': '-.--', 'Z': '--..'}
#
# print('Введите сообщение: ')
# stroka = input().upper().split()   # split преобразует и выводит список upper делает буквы заглавными
# print(stroka)
#
# for i in stroka:
#     for bukva in i:
#         if bukva in MORSE:
#             print(MORSE[bukva], end='')
#     print()    # пустой принт чтобы слова выходили в отдельной строчке


