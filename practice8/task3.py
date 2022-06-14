pairs = [[1,2],[7,8],[4,5]]
pairs.sort()
print(pairs)

def search(seq, i, count=1):
    global pairs
    global maxn

    # Цикл прохода по каждому элементу с i
    for j in range(i+1, len(pairs)):
        # Проверка условия
        if seq[1] < pairs[j][0]:
            maxn = max(maxn, count+1)
            # С этой пары запускаем рекурсивно функцию
            search(pairs[j], j, count+1)        

    
maxn = -1

for i in range(len(pairs)-1):
    search(pairs[i],i)


print(maxn)