from functions import split_data
import statistics
import sys


def read_data_from_file(path :str) -> list:
    data = list()
     
    # пробучаем считать
    try:
        file = open(path, "r")
        print("!")
        with open(path, "r") as file:
            for line in file:
                data.append(line)
    except: # не получается - возвращаем пустой список
        print("Log: can't open or read file")
        return [-1, "Can't open or read"]
    
    cur_data = list()

    for i in range(1, len(data)):
        data[i] = data[i].rstrip()
        # print(data[i])
        
        tmp_data = data[i].split(',')

        if len(tmp_data) != 2:
            return [-2, "Missing data"]

        time, value = tmp_data

        try:
            time = float(time)
            value = float(value)
        except:
            return [-3, "Not a number"]


        # print(time, value)
        cur_data.append([time, value])

    return [0, cur_data]

def calculate_statistics(seg: list) -> dict:
    stats = dict()
    data = list()
    for curr in seg:
        data.append(curr[1])

    stats["start"]  = seg[0][0]
    stats["end"]    = seg[-1][0]
    stats["len"]    = len(seg)
    stats["mean"]   = statistics.mean(data)
    stats["mode"]   = statistics.mode(data)
    stats["median"] = statistics.median(data)

    return stats

def main(path_to_file, interval = 5):
    
    print(path_to_file)
    # Читаем файл
    status, data = read_data_from_file(path_to_file)

    if status < 0: # если список пустой - заканчиваем программу
        print(data)
        return [status, data]
    

    # Делим данные на отрезки с заданным интервалом
    segments = split_data(data, interval)
    output = list()
    # Для каждого отрезка считаем и выводим статистику
    for seg in segments:
        stats = calculate_statistics(seg)
        print(stats)
        output.append(stats)

    for i in range(len(output)-1):
        print((output[i+1]["start"] - output[i]["start"])/60)

    return [0,output]


if __name__ == "__main__":
    path = 'data/example.csv'
    inter = 5
    # Если задан путь к файлу, считываем 
    if len(sys.argv) > 1:
        path = sys.argv[1]

    # Если задан интервал, считываем
    if len(sys.argv) > 2:
        inter = float(sys.argv[2])
    
    main(path, inter)