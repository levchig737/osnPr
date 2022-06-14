# Некорректное услвоие задачи. Если можно использовать нули и единицы, то
# достаточно вывести n 0 или 1. Не сказано вывести все комбинации
# Программа выводит все комбинации без 1 и 0

# Первое решение "в тупую"
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


n = 12
results = []
k = int(n**(1/2))

dif(n, k)
if len(results) == 0:
    print("-1")
else:
    for i in range(len(results)):
        print(results[i])


# Второе решение "Теорема Лагранжа о сумме четырёх квадратов"
# Формулировка: всякое натуральное число можно представить в виде суммы ЧЕТЫРЕХ квадратов целых чисел

n = 50
koren = int(n**(1/2)) + 1
res = []

for i in range(0, koren):
    for j in range(0, koren):
        for k in range(0, koren):
            for m in range(0, koren):
                if i**2 + j**2 + k**2 + m**2 == n:
                    if i != 0:
                        res.append(i)
                    if j != 0:
                        res.append(j)
                    if k != 0:
                        res.append(k)
                    if m != 0:
                        res.append(m)
                    print(res)
                    exit(0)

print(-1)