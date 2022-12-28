def show_menu():
    print("Выберите команду: \n 1 - показать всех сотрудников"
          " \n 2 - добавить сотрудника \n 3 - изменить данные сотрудника \n 4 - удалить сотрудника"
          "5 - импорт-экспорт  данных из csv в csv-файл \n 6 - импорт-экспорт данных из scv в txt-файл")
    try:
        select = int(input())
        if not select in [1, 2, 3, 4]:
            raise ValueError
        return select
    except Exception:
        print("Error")
        exit()


def show_employees(sp):
    print("Список всех сотрудников: ")
    for i, sotr in enumerate(sp, 1):
        print(i, *sotr)


def add_employees():
    print("Введите фамилию, имя и телефон через пробел: ")
    try:
        data = input().split()
        if not '' in data:
            raise ValueError
        return data
    except Exception:
        print("Error")


def change_employees():
    print("Выберите строку для перезаписи: ")
    change = int(input())
    print("Введите строку для записи: ")
    string = input().split()
    return change, string


def delete():
    print("Введите номер строки для удаления: ")
    number = int(input())
    return number


def view_result(sp):
    print("Результат = ", sp)