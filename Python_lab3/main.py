import ctypes

"""
Функция получения массива индексов простых чисел, написанная на си
Получает: Массив
Возвращает: Ничего
"""
def calculate_primes_c(primes):
    lib = ctypes.CDLL('./calculate_primes.so')

    lib.calculate_primes.restype = ctypes.c_voidp
    lib.calculate_primes.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

    ctypes.cast(primes, ctypes.POINTER(ctypes.c_int))

    lib.calculate_primes(primes, m + 1)



""" 
Фунция, выполняющая гипотезу Гольдбаха
Принимает: массив простых чисел
Возвращает: Ничего
"""
def goldbach(primes):
    count = 0

    for i in range(n, m + 1):
        x = 0
        y = 0

        if ((primes[i] != 1) and (i % 2) == 0):
            count = 0
            print(i, end=" ")
            x = 0
            y = 0

            for j in range(2, i//2 + 1):
                if (primes[j] == 1 and primes[i-j] == 1):
                    count += 1
                    if count == 1:
                        x = j
                        y = i - j

                        print(f"{count} {x} {y}")




"""
Тело программы
"""
if __name__ == "__main__":
    n, m = map(int, input().split())
    
    primes = (ctypes.c_int * (m + 1))()

    calculate_primes_c(primes)
    
    goldbach(primes)

