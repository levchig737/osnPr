from ctypes import *

# Загрузка библиотеки
test = CDLL("./libtest.so")

##
# Работа с функциями
##

# Указываем, что функция возвращает int
# test.func_ret_int.restype = ctypes.c_int
# Указываем, что функция принимает аргумент int
# test.func_ret_int.argtypes = [ctypes.c_int, ]

# print('ret func_ret_int: ', test.func_ret_int(101))