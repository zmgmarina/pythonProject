import model_sum as model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()     # получение данных с консоли
    model.init(value_a, value_b)   # инициализация начальных значений
    result = model.sum()         # получение результата от действия
    view.view_data(result, "sum")  #возвращение результата
