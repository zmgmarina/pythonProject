from datetime import datetime as dt # для того чтобы работать с текущей датой импортируем модуль datetime
from time import time

def temperature_logger(data):   # логирование температуры
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:  #создаем файл для записи данных
        file.write('{};temperature;{}\n'
                    .format(time, data))

def pressure_logger(data):        # логирование давления
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};pressure;{}\n'
                    .format(time, data))


def wind_speed_logger(data):   # логирование измерение по скорости ветра
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n'
                    .format(time, data))
