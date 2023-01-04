# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# [‘ПРИВЕТ’, ‘ЗАБВЕНИЕ’, 'ПОКА’] ->[‘ПРИВЕТ’, 'ПОКА’]

import random

# sp = ['ПРИВЕТ', 'ЗАБВЕНИЕ', 'ПОКА']
#
# sp = list(filter(lambda x: 'АБВ' not in x, sp))
# print(sp)

#2 способ:
#
# stroka = input().split()
# res = list(filter(lambda x: 'АБВ' not in x, stroka))
# print(' '.join(res))

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


# Игра на два игрока

# import random
# konf = 100
# name1 = input('Введите свое имя: ')
# name2 = input('Введите свое имя: ')
#
# hod = 0
# move = {0: 'igrok1', 1: 'igrok2'}
#
# player = random.randint(1, 2)
# if player == 1:
#     igrok1 = name1
#     igrok2 = name2
# else:
#     igrok1 = name2
#     igrok2 = name1
#
# print('Первым ходит', igrok1)
#
#
# while konf > 0:
#     if konf > 28:
#         print('Ваш ход', igrok1)
#         count = int(input('Введите количество конфет, не более 28:  '))
#         if count > 28 or count < 1:
#             count = int(input('Вы ввели неверное количество конфет, попробуйте еще раз:  '))
#         konf -= count
#         print('Осталось', konf, 'штук')
#         if konf > 28:
#             print('Ваш ход', igrok2)
#             count = int(input('Введите количество конфет, не более 28:  '))
#             if count > 28 or count < 1:
#                 count = int(input('Вы ввели неверное количество конфет, попробуйте еще раз:  '))
#             konf -= count
#             print('Осталось', konf, 'штук')
#             if konf <= 28:
#                 if hod == 0:
#                     print(igrok1, 'забирает оставшиеся конфеты и побеждает')
#                 if hod == 1:
#                     print(igrok2, 'забирает оставшиеся конфеты и побеждает')
#         else:
#             if hod == 0:
#                 print(igrok2, 'забирает оставшиеся конфеты и побеждает')
#             else:
#                 print(igrok1, 'забирает оставшиеся конфеты и побеждает')
#
#
# # Игра с ботом
#
# import random
# konf = 100
# bot = random.randint(1, 28)
# hod = 0
# move = {0: 'player', 1: 'bot'}
#
#
# while konf > 0:
#     if konf > 28:
#         player = int(input('Ваш ход, player, введите количество конфет, не более 28:  '))
#         konf = konf - player
#         print('Осталось', konf, 'штук')
#         if konf > 28:
#             print('Ход бота: ', bot)
#             konf = konf - bot
#             print('Осталось', konf, 'штук')
#             if konf <= 28:
#                 if hod == 0:
#                     print('player забирает оставшиеся конфеты и побеждает')
#                 if hod == 1:
#                     print('bot забирает оставшиеся конфеты и побеждает')
#         else:
#             if hod == 0:
#                 print('bot забирает оставшиеся конфеты и побеждает')
#             else:
#                 print('player забирает оставшиеся конфеты и побеждает')
#
#
# # УМНЫЙ БОТ
#
# import random
# konf = 100
# hod = 0
# move = {0: 'Игрок', 1: 'Бот'}
#
#
# while konf > 0:
#     if konf > 28:
#         count = int(input('Ваш ход, Игрок, введите количество конфет, не более 28:  '))
#         konf = konf - count
#         print('Осталось', konf, 'штук')
#         if konf > 28:
#             print('Ход бота')
#             count = konf % 29
#             if count == 0:
#                 count = random.randint(1, 28)
#             konf = konf - count
#             print('Бот взял', count, 'конфет', 'сталось,', konf, 'штук')
#             if konf <= 28:
#                 if hod == 0:
#                     print('Игрок забирает оставшиеся конфеты и побеждает')
#                 if hod == 1:
#                     print('Бот забирает оставшиеся конфеты и побеждает')
#         else:
#             if hod == 0:
#                 print('Бот забирает оставшиеся конфеты и побеждает')
#             else:
#                 print('Игрок забирает оставшиеся конфеты и побеждает')
#
#
#
# #
# # 3. Создайте программу для игры в "Крестики-нолики".
#
# sp = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# def pole(sp):
#     for i in range(len(sp)):
#         print(sp[i])
#
# position = { 1: (0, 0), 2: (0, 1), 3: (0, 2),
#              4: (1, 0), 5: (1, 1), 6: (1, 2),
#              7: (2, 0), 8: (2, 1), 9: (2, 2)}
#
# hod = 0
# move = {0: 'x', 1: '0'}
#
# player = random.randint(1, 2)
# if player == 1:
#     igrok1 = 'x'
#     igrok2 = '0'
# else:
#     igrok1 = '0'
#     igrok2 = 'x'
#
# print('Первым ходит', igrok1)
#
# def win_pos(sp):
#     if any(i[0] == i[1] == i[2] for i in sp):
#         return True
#     if any(a == b == c for a, b, c in zip(*sp)):
#         return True
#     if sp[0][0] == sp[1][1] == sp[2][2] or sp[0][2] == sp[1][1] == sp[2][0]:
#         return True
#     return False
#
#  while True:
#     pole(sp)
#     print({'Ваш ход', move[hod]})
#     a = int(input('Выберите позицию для хода: '))
#     m, n = position[a]
#     sp[m][n] = move[hod]
#     if win_pos(sp):
#         pole(sp)
#         print(move[hod], ', вы победили')
#         break
#     hod = (hod + 1) % 2
#
#
# # 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # Пример:
# # Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# # Текст после кодировки: 12W1B12W3B24W1B14W#
# # Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# # Входные и выходные данные хранятся в отдельных текстовых файлах
#
# with open('file_code.txt', 'w') as data:
#     data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
#
# path = 'file_code.txt'
# data = open(path, 'r')
# text = data.readline()
#
# count = 1
# res_text = ''
#
# # текст после кодировки
# for i in range(1, len(text)):
#     if text[i] == text[i - 1]:
#         count += 1
#     else:
#         res_text += str(count) + text[i - 1]
#         count = 1
# res_text += str(count) + text[i]
#
# with open('code.txt', 'w') as data:
#     data.write(res_text)
#
#  # текст после дешифровки
# with open("code.txt", "r") as data:
#     text = data.readline()
#
# digit = ''
# res = ''
# for i in range(0, len(text)):
#     if text[i].isdigit():
#         digit += text[i]
#     else:
#         res += int(digit) * text[i]
#         digit = ''
#
# with open('decode.txt', 'w') as data:
#     data.write(res)





