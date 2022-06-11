"""
- 3 точки
- 0-255
- Без 1-rо 0
- от 1 до 3 символов
"""

s_ip = "25525511135"
res = []
s = ""

def check(s,count):
    if s[0] == 0 or int(s[0]) > 2:
        return False
    if len(s) > (3-count)*3 and count != 3:
        return False
    return True

def make_ip(s):
    None


i = -1
start = 0
while i < len(s_ip)-2:
    i += 1
    if s_ip[i] == 0 and start == i:
        continue
    if len(res) == 3:
        if check(s_ip[start:],len(res)):
            print("hi")
            res.append(s_ip[start:])
            break
    if not check(s_ip[(i+1):],len(res)):
        # res.clear()
        continue

    res.append(s_ip[start:(i+1)])
    print(start,i, res)
    start = i + 1

print(res)


