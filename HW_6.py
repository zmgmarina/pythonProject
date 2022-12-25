# 1.	Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел.
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.
# Входные данные	Выходные данные
# 36                  6
# 12
# 144
# 18
import math
sp = []
i = 0
while i != ' ':
    i = input(f'Введите числa: ')
    sp.append(i)

sp = ' '.join(sp).split()

sp = [int(i) for i in sp]

sp2 = []
for el in range(len(sp)):
    for j in range(el, len(sp)):
       sp2.append(math.gcd(sp[el], sp[j]))

print(f"НОД списка чисел является: {min(sp2)}")


# 2.	Орел и решка
#
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла,
# а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
#
# Формат входных данных:
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

# Формат выходных данных:
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.

# Входные данные	                                        Выходные данные
# ОРРОРОРООРРРО	                                                3
# ООООООРРРОРОРРРРРРР                                           7
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР  	31

str = input('Введите буквы "О" и "Р" в произвольном порядке: ')
print(str)

sp = []
count = 0
for i in str:
    if i == 'Р':
        count += 1
    if i != 'Р':
        sp.append(count)
        count = 0
sp.append(count)
print(max(sp))

for i in str:
    if i != 'Р':
        print('0')
        break




# 3.	Задача
# Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ), применив лямбды, filter, map, zip, enumerate, списочные выражения.


# 1.	Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# Входные данные	Выходные данные
# 1 2 2 3 3 3	     1

list = [1, 2, 2, 3, 3, 3]

new_list = []
for i in list:
    if list.count(i) == 1:
        new_list.append(i)
print(*new_list) # * распаковывает (выводит из скобок) список

# c выражением:
list = [1, 2, 2, 3, 3, 3]
new_list = [i for i in list if list.count(i) == 1]
print(*new_list)







