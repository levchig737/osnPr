import csv
import statistics
import sys

from split_data_function import split_data
from pathlib import Path



"""
Чтение файла .csv
Принимает путь к файлу
Возвращает двумерный список из float элементов [time, value]
"""
def read_data_from_file(path):
    data = []

    #  Проверка на тип файла
    if Path(path).suffix != '.csv':
        return  [-3, "Isn't .csv file"]

    # Проверка исключений
    try:
        # Чтение файла
        with open(path) as file:
            data_reader = csv.reader(file)
            for i in data_reader:

                # Проверка на пустую колонку
                if len(i) != 2:
                    return [-4, "Missing data"]

                data.append(i)
            data.pop(0)
    
    # Проверка на существования файла
    except FileNotFoundError:
        return [-1, "Not found"]

    # Проверка на возможность чтения
    except PermissionError:
        return [-2, "Can't read"]

    result_array = []

    # Преобразование к типу float
    try:
        for i in range(len(data)):
            result_array.append(list(map(float, data[i])))
    except ValueError:
        return [-4, "Missing data"]
    return [0, result_array]


"""
Подсчет статистики отрезка
Принимает список - отрезок
Возвращае словарь cо статистикой
"""
def calculate_statistics(segment):
    data_statistics = dict()
    
    # Массив с value переданного сегмента
    data = []

    for i in segment:
        data.append(i[1])

    data_statistics["start"] = segment[0][0]
    data_statistics["len"] = len(segment)
    data_statistics["mean"] = statistics.mean(data)
    data_statistics["mode"] = statistics.mode(data)
    data_statistics["median"] = statistics.median(data)
    data_statistics["end"] = segment[len(segment)-1][0]
    
    return data_statistics


def main(path = "data/example.csv", interval = 5):

    # Чтение файла
    res, data = read_data_from_file(path)
    
    if res != 0:
        print(data)
        return [res, data]

    # Преобразование данных во временные отрезки
    segments = split_data(data, interval)

    output = []

    # Вывод статистики
    for i in range(len(segments)):
        stats = calculate_statistics(segments[i])
        print(stats)
        output.append(stats) 

    return [0, output]


# Основное тело программы
if __name__ == "__main__":

    path = "data/example.csv"
    interval = 5

    # Аргументы командой строки
    if len(sys.argv) != 1:
        if len(sys.argv) > 1:
            path = sys.argv[1]
        if len(sys.argv) > 2:
            interval = sys.argv[2]

    res, output = main(path, interval)
