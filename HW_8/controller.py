import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding="utf-8")


def main():
    try:
        select = view.show_menu()
        if select == 1:
            logging.info("Выбран режим - 1")
            sotr = model.get_list()
            view.show_employees(sotr)
            logging.info("Данные получены")
        elif select == 2:
            logging.info("Выбран режим - 2")
            data = view.add_employees()
            model.add_employees_to_list(data)
            logging.info("Данные получены")
        elif select == 3:
            logging.info("Выбран режим - 3")
            change, string = view.change_employees()
            model.update_employees(change, string)
            logging.info("Данные получены")
        elif select == 4:
            logging.info("Выбран режим - 4")
            number = view.delete()
            model.delete(number)
            logging.info("Данные получены")
    except Exception:
        logging.warning("Ошибка ввода!")



