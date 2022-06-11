strs = ["flower","flow","flight"]

j = -1
flag = True
res = ""
while flag:
    j += 1
    if len(strs[0]) <= j:
        break

    simvol = strs[0][j]
    for i in strs:
        if len(i) <= j:
            flag = False
            break
        if i[j] != simvol:
            flag = False
            break
    
    if flag:
        res += simvol

print(res)