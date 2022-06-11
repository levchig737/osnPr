"""
- 3 точки
- 0-255
- Без 1-rо 0
- от 1 до 3 символов
"""

# s_ip = "25525511135"
# res = []
# s = ""

# def check(s,count):
#     if s[0] == 0 or int(s[0]) > 2:
#         return False
#     if len(s) > (3-count)*3 and count != 3:
#         return False
#     return True

# def make_ip(s):
#     None


# i = -1
# start = 0
# while i < len(s_ip)-2:
#     i += 1
#     if s_ip[i] == 0 and start == i:
#         continue
#     if len(res) == 3:
#         if check(s_ip[start:],len(res)):
#             print("hi")
#             res.append(s_ip[start:])
#             break
#     if not check(s_ip[(i+1):],len(res)):
#         # res.clear()
#         continue

#     res.append(s_ip[start:(i+1)])
#     print(start,i, res)
#     start = i + 1

# print(res)


a = "25525511135"
ans = []

def check(t):
    if len(t) < 4 and int(t) < 256 and len(t) > 0:
        return not (len(t) > 1 and t[0] == " ")
    else:
        return False

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