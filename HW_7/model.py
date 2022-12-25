import csv


def import_file():
    sp = []
    with open("file.csv", encoding='utf-8') as r_file:
        reader_object = csv.reader(r_file, delimiter = ",")
        for row in reader_object:
            sp.append(row)
    return sp


def export_file(sp):
    with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        for row in sp:
            file_writer.writerow(row)


def export_file_for_txt(sp):
    with open('file.txt', 'w', encoding="utf-8") as data:
        for i in sp:
            for j in i:
                data.write(str(j))
                data.write('\n')
            data.write('\n')

