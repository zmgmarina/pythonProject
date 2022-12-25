def greeting():
    print("Привет! Выберите действие: 1-импорт-экспорт  данных из csv в csv-файл, 2-импорт-экспорт данных из scv в txt-файл")
    select = int(input())
    return select


def view_result(sp):
    print("Результат = ", sp)

