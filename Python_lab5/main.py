import csv
import statistics
import sys
from split_data_function import split_data




"""
Чтение файла .csv
Принимает путь к файлу
Возвращает двумерный список из float элементов [time, value]
"""
def read_data_from_file(path):
    data = []

    # Проверка исключений
    try:
        # Чтение файла
        with open(path) as file:
            data_reader = csv.reader(file)
            for i in data_reader:
                data.append(i)
            data.pop(0)
    
    # Проверка на существования файла
    except FileNotFoundError:
        return [-1, "Not found"]

    # Проверка на возможность чтения
    except PermissionError:
        return [-2, "Can't read"]

    # Преобразование к типу float
    result_array = []
    for i in range(len(data)):
        result_array.append(list(map(float, data[i])))
    
    return [0, result_array]


"""
Подсчет статистики отрезка
Принимает список - отрезок
Возвращае словарь cо статистикой
"""
def calculate_statistics(segment):
    data_statistics = dict()
    data_statistics["len"] = len(segment)
    data_statistics["mean"] = statistics.mean(segment[1])
    data_statistics["mode"] = statistics.mode(segment[1])
    data_statistics["median"] = statistics.median(segment[1])
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
    for i in range(len(segments)-1):
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
    