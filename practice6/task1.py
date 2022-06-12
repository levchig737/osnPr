def to7(num, osn=7):
    res = ""
    flag = False
    if num == 0:
        return "0"
    if num < 0:
        flag = True
        num = num-num*2

    while num > 0:
        res = str(num%osn) + res
        num //= osn

    if flag:
        res = "-" + res
    return res
    

num = 100
print(to7(num))