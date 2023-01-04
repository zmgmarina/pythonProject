import csv
# чтение csv-файла

# with open("file-csv.csv", encoding='utf-8') as r_file:
#     reader = csv.reader(r_file, delimiter=",")  # reader - функция возвращающая обьект чтения, в него передаем csv-файл  разделитель
#     title = next(reader)  # функция next считывает первую строку(заголовок), если он не нужен и помещает в переменную title
#     sp = list(reader)     # оставшиеся строки в reader помещаем в список
#     for row in sp:
#         print(row)        # перебираем список, распечатываем строки


# #чтение в словарь
# with open("file-csv.csv", encoding='utf-8') as r_file:
#     reader = csv.DictReader(r_file, delimiter=",")
#     expensive = sorted(reader, key=lambda x: int(x['цена']), reverse=True) # отсортировали по умолчанию(True) по убыванию
# print(expensive)  # получили список словарей
# print()
# for record in expensive:
#     print(record)

# запись  в файл ( для перезаписи режим 'w')

# with open("file-csv.csv", 'a', encoding='utf-8', newline='') as r_file: #newline позволяет избавиться от новых строк
#     writer = csv.writer(r_file, delimiter=",")
#     row = ['колбаса', 500, 'микоян']
#     row1 = ['йогурт', 34, 'данон']
#     writer.writerow(row)
#     writer.writerow(row1)
#


# запись словаря в файл cvs

data = [{
    'lastname': 'Иванов',
    'firstname': 'Петр',
    'class_number': '9',
    'class_letter': 'A'
}, {
    'lastname': 'Петров',
    'firstname': 'Олег',
    'class_number': '9',
    'class_letter': 'B'
}, {
    'lastname': 'Кузнецов',
    'firstname': 'Андрей',
    'class_number': '9',
    'class_letter': 'A'
}]

with open("dictwriter.csv", 'w', encoding='utf-8', newline='') as f: # создаем файл
    writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), delimiter=',') # передаем в него fieldname - наименования столбцов(берем data[0](1 словарь) и его ключи, передаем в первую строчку(шапка)
    writer.writeheader()  # заголовки записали
    for d in data:  # все остальные данные записываются в последующие строчки
        writer.writerow(d)





