import csv
import statistics
import sys
from split_data_function import split_data


# Чтение файла .csv
# Принимает путь к файлу
# Возвращает двумерный список из float элементов [time, value]
def read_data_from_file(path):
    data = []
    with open(path) as file:
        data_reader = csv.reader(file)
        for i in data_reader:
            data.append(i)
        data.pop(0)

        # Преобразование к типу float
        result = []
        for i in range(len(data)):
            result.append(list(map(float, data[i])))
    return result


# Подсчет статистики отрезка
# Принимает список - отрезок
# Возвращае словарь со статистикой
def calculate_statistics(segment):
    data_statistics = dict()
    data_statistics["len"] = len(segment)
    data_statistics["mean"] = statistics.mean(segment[1])
    data_statistics["mode"] = statistics.mode(segment[1])
    data_statistics["median"] = statistics.median(segment[1])
    return data_statistics


# Основное тело программы
if __name__ == "__main__":

    interval = 5
    path = "example.csv"

    # Аргументы командой строки
    if len(sys.argv) != 1:
        path = sys.argv[1]
        interval = sys.argv[2]

    # Чтение файла
    data = read_data_from_file(path)

    # Преобразование данных во временные отрезки
    segments = split_data(data, interval)

    # Вывод статистики
    for i in range(len(segments)-1):
        print(calculate_statistics(segments[i]))
