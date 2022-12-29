import csv


def get_list():
    with open("data.csv", encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=",")
        return list(reader)


def add_employees_to_list(employees):
    with open("data.csv", 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(employees)


def update_employees(number, string):
    try:
        with open("data.csv", 'r', encoding="utf8", newline='') as file:
            reader = csv.reader(file, delimiter=",")
            data = list(reader)
            data[number] = string
        with open("data.csv", 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=",")
            for i in data:
                writer.writerow(i)
    except IndexError:
        print("Вы вышли за границы списка")
        exit()
    except Exception:
        print("Ошибка")
        exit()

def delete(number):
    try:
        with open("data.csv", 'r', encoding="utf8", newline='') as file:
            reader = csv.reader(file, delimiter=",")
            data = list(reader)
            del data[number]
        with open("data.csv", 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=",")
            for i in data:
                writer.writerow(i)
    except IndexError:
        print("Вы вышли за границы списка")
        exit()
    except Exception:
        print("Ошибка")
        exit()



def import_file():
    sp = []
    with open("data.csv", encoding='utf-8') as file:
        reader_object = csv.reader(file, delimiter = ",")
        for row in reader_object:
            sp.append(row)
    return sp


def export_file(sp):
    with open("file.csv", mode="w", encoding='utf-8') as w_file:
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
