# Некорректное услвоие задачи. Если можно использовать нули и единицы, то
# достаточно вывести n 0 или 1. Не сказано вывести все комбинации
# Программа выводит все комбинации без 1 и 0
def dif(summ, k, res = []):
    global results
    for i in range(k, 1, -1):
        summ1 = summ - i ** 2
        r = int(summ1**(1/2))
        if summ <= 1:
            res.clear()
            break
        if summ1 == 0 or summ == 0:
            res.append(i)
            res.sort()
            if res not in results:
                results.append(res)
            return 1
        else:
            res.append(i)
            # print(res,i, summ, summ1, r)
            dif(summ1, r, res.copy())
            res.clear()
    return 0

n = 13
summ = 0
results = []
k = int(n**(1/2))

dif(n, k)
if len(results) == 0:
    print("-1")
else:
    for i in range(len(results)):
        print(results[i])
