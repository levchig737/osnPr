s1 = "aooob"
s2 = "eidboaoo"

s1 = sorted(s1)
flag = False

for i in range(len(s2)-len(s1)+1):
    string = s2[i:i+len(s1)]
    if s1 == sorted(string):
        flag = True
        break

print(flag)