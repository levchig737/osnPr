import csv
import statistics
import sys
from split_data_function import split_data


# Чтение файла .csv
# Принимает путь к файлу
# Возвращает двумерный список из float элементов [time, value]
def read_data_from_file(path):       #функция, возвращающая набор строк
    data = []
    with open(path) as file:            #чтение файла
        data_reader = csv.reader(file)   
        for i in data_reader:
            data.append(i)

        data.pop(0) # Удаление со сдвигом первого элемнта ['time','value']

        # Преобразование к типу float
        result = []                    #создание массива
        for i in range(len(data)):     #диапазон количества значений
            result.append(list(map(float, data[i])))   # Преобразуем оба элемента по индексу i к типу float, и после оба их к типу list и добавялем в result 
    return result


# Подсчет статистики отрезка
# Принимает список - отрезок
# Возвращает словарь со статистикой
def calculate_statistics(segment):
    data_statistics = dict() # список со статистикой по ключу - значение
    
    data = []  # Массив с value переданного сегмента

    for i in segment:
        data.append(i[1])

    data_statistics["len"] = len(segment)               # Длина/кол-во элементов сегмента
    data_statistics["mean"] = statistics.mean(data)     # Среднее зн-е value сегмента
    data_statistics["mode"] = statistics.mode(data)     # Мода
    data_statistics["median"] = statistics.median(data) # Медиана
    return data_statistics


# Основное тело программы (оно вполняется первым)
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
