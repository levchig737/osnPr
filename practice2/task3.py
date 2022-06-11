# Некорректное условие, т.к. все числа деляться на 1
# Условие: n число из тех, которые деляться только на 2, 3 или 5
from math import sqrt

def prostie(start, end, pr):
    for i in range(start, end):
        for j in pr:
            if j > int((sqrt(i)) + 1):
                pr.append(i)
                break
            if (i % j == 0):
                break
        else:
            pr.append(i)


n = 10
pr = []
prostie(2,n,pr)
print(pr)

res = []
i = 1
while len(res) != n:
    i += 1
    if i > pr[len(pr)-1]:
        prostie(i, i*2, pr)
        i -= 1
        continue 

    if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0):
        continue
    
    for j in pr:
        if j == 3 or j == 5 or j == 2:
            continue
        if i % j == 0:
            break

    res.append(i)
    
print(pr)
print(res)
print(len(res))
print(res[len(res)-1])
