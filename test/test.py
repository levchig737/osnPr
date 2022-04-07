from functions import split_data
import statistics
import sys

# Принимает путь к файлу
# Возвращает список строк этого файла
def read_data_from_file(path : str) -> list:
    data = list()
    file = open(path, "r")
    with open(path, "r") as file:
        for line in file:
            data.append(line)

    for i in range(len(data) - 1):
        data[i] = data[i].strip()
    
    return data

# Принимает список значений
# Возвращает статистику по этому списку
def calculate_statistics(seg: list) -> dict:
    stats = dict()

    stats["start"]  = seg[0][0]
    stats["end"]    = seg[len(seg)-1][0]
    stats["len"]    = len(seg)
    stats["mean"]   = statistics.mean(seg[1])
    stats["mode"]   = statistics.mode(seg[1])
    stats["median"] = statistics.median(seg[1])
    
    return stats


if __name__ == "__main__":
    path_to_file = "example.csv"
    
    interval = 5

    # Если задан путь к файлу, считываем
    if len(sys.argv) > 1: 
        path_to_file = sys.argv[1]
    
    # Если задан интервал, считываем
    if len(sys.argv) > 2:
        interval = float(sys.argv[2])

    # Читаем файл
    data = read_data_from_file(path_to_file)

    # Делим данные на отрезки с заданным интервалом
    segments = split_data(data, interval)

    # Для каждого отрезка считаем и выводим статистику
    for i in range(len(segments)):
        stats = calculate_statistics(segments[i])
        print(stats)
