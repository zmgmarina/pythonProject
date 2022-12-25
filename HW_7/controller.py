import view
import model
import logging


logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding="utf-8")


def main_func():
    try:
        select = view.greeting()
        if select == 1:
            logging.info("Выбран режим импорт-экспорт  данных из csv в csv-файл")
            sp = model.import_file()
            resulte = model.export_file(sp)
            view.view_result(sp)
            logging.info("Получен результат")
        elif select == 2:
            logging.info("Выбран режим импорт-экспорт данных из scv в txt-файл")
            sp = model.import_file()
            resulte = model.export_file_for_txt(sp)
            view.view_result(sp)
            logging.info("Получен результат")
    except Exception:
        logging.warning("Ошибка ввода!")
