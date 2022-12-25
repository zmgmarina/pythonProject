import view
import model
import logging


logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding="utf-8")


def main_function():
    try:
        select = view.greeting()
        if select == 1:
            logging.info("Выбран режим калькулятор")
            example = view.get_math_example()
            result = model.calc(example)
            view.view_result(result)
            logging.info("Получен результат вычисления")
        elif select == 2:
            logging.info("Выбран режим конвертер")
            massa = view.get_massa()
            logging.info("Введено значение")
            value = model.convert(massa)
            view.view_result(value)
            logging.info("Получен результат вычисления")
    except Exception:
        logging.warning("Ошибка ввода!")





