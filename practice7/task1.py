"""
Проверить:
- длины каждой стороны ==
- каждый угол == 90 градусов или скалярное произведение векторов = 0
"""

"""
Функция подсчета квадрата длины стороны
"""
def dlina(x1, x2, y1, y2):
    return (x1-x2)**2 + (y1-y2)**2


"""
Функция подсчета скалярного произведения векторов
"""
def sp(p1, p2, p3):
    v1 = [p2[0]-p1[0], p2[1]-p1[1]]
    v2 = [p3[0]-p2[0], p3[1]-p2[1]]
    return v1[0]*v2[0]+v1[1]*v2[1]


p1 = [3, 0]
p2 = [4, 3]
p3 = [7, 2]
p4 = [6, -1]

a1 = dlina(p1[0],p2[0],p1[1],p2[1])
a2 = dlina(p2[0],p3[0],p2[1],p3[1])
a3 = dlina(p3[0],p4[0],p3[1],p4[1])
a4 = dlina(p4[0],p1[0],p4[1],p1[1])

# Если есть 1 угол 90 и все стороны равны, то это квадрат
# Если скалярное произведение векторов == 0, то cos угла == 0, т.е. угол == 90
res = sp(p1,p2,p3)

print(a1==a2==a3==a4 and res == 0)