# Преобразует данных во временные отрезки длиной interval
# Принимает двумерный список элементов [time, value], интервал
# Возвращает трехмерный спиское элементов [[time, value],...,[time,value]]
def split_data(data, interval):
    segments = []           #массив сегментов
    cur_seg = []         #нынешний сегмент
    len_data = len(data)   #количество данных/строк
    start_time = data[0][0]   #начало времени, задаём массив данных

    for i in range(0, len_data):  #диапазон
        cur_time = data[i][0]
        if (cur_time - start_time) <= float(interval) * 60:     # условие отрезка в interval минут
            cur_seg.append(data[i])
        else:
            start_time = cur_time
            segments.append(cur_seg.copy()) #copy т.к. список не копируется при добавлении в другой список
            cur_seg.clear() #эквивалентно cur_seg = []
            cur_seg.append(data[i])
    segments.append(cur_seg)
    return segments
