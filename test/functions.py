# Принимает список строк и интервал
# Возвращает список списков данных, разделённые по заданному интервалу
def split_data(data: list, interval_in_min: int = 5) -> list:
    segments = list()
    cur_seg = list()
    
    cur_time = float(data[1].split(',')[0])
    
    for i in range(1,len(data)):
        cur_str = data[i]

        time, count = map(float, cur_str.split(','))

        if (time - cur_time) <= (interval_in_min * 60.0):
            cur_seg.append([time, count])
        else:
            segments.append(cur_seg)
            cur_seg = list()
            cur_seg.append([time, count])
            cur_time = time

    segments.append(cur_seg)

    return segments
