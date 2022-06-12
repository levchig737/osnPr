"""
Функция проверки отрезка ip
"""
def check(t):
    if len(t) < 4 and int(t) < 256 and len(t) > 0:
        # return not (len(t) > 1 and t[0] == " ")
        return True
    else:
        return False


a = "101023"
ans = []

for i1 in range(0, min(3,len(a)-3)):
    a1 = a[0:i1+1]
    if check(a1):
        for i2 in range(i1+1,len(a)-2):
            a2 = a[i1+1:i2+1]
            if check(a2):
                for i3 in range(i2+1,len(a)-1):
                    a3 = a[i2+1:i3+1]
                    a4 = a[i3+1:]
                    if check(a3):
                        ans.append(".".join([a1,a2,a3,a4]))

print(ans)