"""
Преобразует данных во временные отрезки длиной interval
Принимает двумерный список элементов [time, value], интервал
Возвращает трехмерный спиское элементов [[time, value],...,[time,value]]
"""
def split_data(data, interval):
    segments = []
    cur_seg = []
    len_data = len(data)
    start_time = data[0][0]

    for i in range(0, len_data):
        cur_time = data[i][0]
        if (cur_time - start_time) <= float(interval) * 60:
            cur_seg.append(data[i])
        else:
            start_time = cur_time
            segments.append(cur_seg.copy())
            cur_seg.clear()
            cur_seg.append(data[i])
    segments.append(cur_seg)
    print(segments[1])
    return segments
