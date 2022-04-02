import re
from turtle import st
import pytest
from main import *
from split_data_function import *
from math import ceil



"""
    Тест на отсутсвие передаваемого файла
"""
def test_no_file():
    res, data = read_data_from_file("wrong_path.csv")
    assert res == -1, "No such file"


"""
    Тест на отстутсвия прав на чтения передаваемого файла
"""
def test_no_read():
    res, data = read_data_from_file("data/file_without_read.csv")
    assert -2 == res, "Can't read"


"""
    Тест на файл не .csv
"""
def test_not_csv():
    res, data = read_data_from_file("data/file.txt")
    assert -3 == res, "Isn't .csv"


"""
    Тест на одну колонку в файле
"""
def test_one_column():
    res, data = read_data_from_file("data/one_column.csv")
    assert -4 == res, "One column"


"""
    Тест на данные не заданного типа
"""
def test_not_float():
    res, data = read_data_from_file("data/no_float_int.csv")
    assert -4 == res, "Not float"


"""
    Тест на правильные временные отрезки
"""
def test_right_seg_time():
    res, data = main()
    if res != 0:
        assert False
        
    for i in range(0, len(data)-1):
        if abs(data[i+1]["start"] - data[i]["start"]) < 5 * 60.0:
            assert False, "False seg"

    assert True


"""
    Тест на правильное кол-во интерваллов
"""
def test_right_intervals():
    res, data = main()
    cur_len = (data[-1]["end"] - data[0]["start"]) / (5 * 60)
    cur_len = ceil(cur_len)
    assert (res == 0 and cur_len == len(data) )


"""
    Тест на правильный подсчет статистики
"""
def test_right_statisticks():
    data = [
      [301.0703125, 234.0], 
      [301.984375, 234.0], 
      [302.953125, 248.0], 
      [303.953125, 256.0], 
      [304.93359375, 251.0], 
      [305.91796875, 253.0],    
    ]

    # 234 234 248 251 253 256 257 Mediana

    statisticks = {
        "start": 301.0703125,
        "len": 6,
        "mean": 246.0,
        "mode": 234.0,
        "median": 249.5,
        "end": 305.91796875
    }
    res = calculate_statistics(data)
    assert res == statisticks, "Wrong statisticks"
