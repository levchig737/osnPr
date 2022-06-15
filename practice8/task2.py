# Фукнция добавления в массивы положительный значений и создание отрицательных
def pol(sp, otric):
    global sp_x, sp_nums
    for i in range(len(sp)):
        if '-' in sp[i]:
            otric = otric + sp[i].split("-")[1:] # Делим строку с - и добавляем в список отриц. без 1го(он полож.)
            sp[i] = sp[i][0]   
        
        # Х обрабатываем отдельно, могут быть 2x и т.п.    
        if 'x' in sp[i]:
            if len(sp[i]) != 1:
                sp_x.append(sp[i][:-1])
            else:
                sp_x.append('1')
        else:
            # Если x нет то это число
            sp_nums.append(sp[i])

    return otric

# Функция обработки отричцательных зачний и добавления их с - в массивы
def otr(sp):
    global sp_x, sp_nums
    for i in range(len(sp)):
        # Х обрабатываем отдельно, могут быть 2x и т.п.    
        if 'x' in sp[i]:
            if len(sp[i]) != 1:
                sp_x.append('-' + sp[i][:-1])
            else:
                sp_x.append('-1')
        else:
            # Если x нет то это число
            sp_nums.append('-' + sp[i])

# Сумма списка
def summ(sp):
    res = 0
    for i in sp:
        res += int(i)
    return res


s = "x+5-3+x=6+x-2"

# Разделили уравнение на левую и правую части
a1 = s.split('=')
a2 = a1[1]
a1 = a1[0]

# Коэффициенты перед x и числа
sp_x = []
sp_nums = []

# Получаем положительные элементы и выражения с - из Левой стороны
poloz = a1.split("+")
otric = []

# Левая часть положительные
otric = pol(poloz, otric)

# Левая часть с отрицательными
otr(otric)

# Считаем суммы
summ_x = summ(sp_x)
summ_nums = summ(sp_nums)

# Очищаем
sp_nums.clear()
sp_x.clear()


# Теперь правая сторона
poloz = a2.split("+")
otric = []

# Правая часть положительные
otric = pol(poloz, otric)

# Правая часть с отрицательными
otr(otric)

# Считаем суммы
summ_x -= summ(sp_x)       # Минус т.к. в левую переносим
summ_nums -= summ(sp_nums)

# резульатт
if summ_x == 0:
    if summ_nums == 0:
        print("Бесконечное множество решений")
    else:
        print("Нет решений")
else:
    print(f"x={-summ_nums/summ_x}")

