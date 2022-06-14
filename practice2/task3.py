# Условие: n число из тех, которые деляться только на 2, 3 или 5

def delit(num):
    # Делим на 5 пока нет остатка
    while num % 5 == 0:
        num //= 5
    # Делим на 3 пока нет остатка
    while num % 3 == 0:
        num //= 3
    # Делим на 2 пока нет остатка
    while num % 2 == 0:
        num //= 2

    return num
    

n = 10
count = 0
i = 1

while count < n:
    res = delit(i)
    if res == 1:
        count += 1
        print(i)

    i += 1