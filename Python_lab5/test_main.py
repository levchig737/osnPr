import pytest
from main import *
from split_data_function import *




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
