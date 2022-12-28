import csv


def get_list():
    with open("data.csv", encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=",")
        return list(reader)


def add_employees_to_list(employees):
    try:
        with open("data.csv", 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(employees)
    except Exception:
        print("Неверный формат ввода, попробуйте еще раз")


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
    with open("data.csv", 'r', encoding="utf8", newline='') as file:
        reader = csv.reader(file, delimiter=",")
        data = list(reader)
        del data[number]
    with open("data.csv", 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        for i in data:
            writer.writerow(i)

