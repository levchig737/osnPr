from main import *
from functions import *
from math import ceil

#
#   Тест на то, что правильно считывает обычный входной пример
#
def test_on_example():
    status, data = main(path_to_file="./data/example.csv", interval=5);
    assert status == 0


#
#   Тест на отсутствие файла
#
def test_no_file():
    data = main(path_to_file="a.py")
    assert data == [-1,  "Can't open or read"]


#
#   Тест на файл без права чтения
#
def test_no_read():
    data = main(path_to_file="./data/data.csv")
    assert data == [-1, "Can't open or read"]


#
#   Тест на файл не текстовый, в данном случае - картинка
#
def test_not_csv():
    data = main(path_to_file="data/butterfly-clip-art-blue-butterfly-590049.png")
    assert data == [-1, "Can't open or read"]


#
#   Тест на входные данные, где на какой-то строке не будет одного значения
#
def test_some_spaces():
    data = main(path_to_file="./data/data_with_spaces.csv")
    assert data == [-2, "Missing data"]
    

#
#   Тест на входные данные, где каоке-либо значение не является числом
#
def test_diff_type():
    data = main(path_to_file="./data/data_with_dt.csv")
    assert data == [-3, "Not a number"]


#
#   Тест на то что split_data правильно делит на временные отрезки
#
def test_good_seg_on_time():
    status, data = main(path_to_file='./data/example.csv', interval=5)
    if status != 0:
        assert False
        
    for i in range(1, len(data)):
        if abs(data[i]["start"] - data[i-1]["start"]) < 5 * 60.0:
            assert False

    assert True


#
#   Тест на число отрезков
#
def test_good_cnt_of_seg():
    status, data = main(path_to_file="./data/example.csv", interval=5)
    cur_len = ( data[-1]["end"] - data[0]["start"] ) / (5 * 60)
    cur_len = ceil(cur_len)
    assert (status == 0 and 
            cur_len == len(data) )


#
#   Тест на правильность подсчёта статистики
#
def test_current_stats():
    cur_data = [[571.1328125,1],
                [572.0703125,2],
                [573.02734375,3],
                [573.953125,4],
                [574.87890625,5]]
    cur_stats = {'start':571.1328125, 
                 'end': 574.87890625, 
                 'len': 5, 
                 'mean': 3, 
                 'mode': 1, 
                 'median': 3}
    assert calculate_statistics(cur_data) == cur_stats
    