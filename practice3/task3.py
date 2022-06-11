s = ["eat","tea","tan","ate","nat","bat"]
s2 = []
res = []
res2 = []

for i in s:
    s2.append(sorted(i))

for i in range(len(s)):
    if s2[i] in res:
        continue
    res2.append([])
    for j in range(i,len(s)):
        if s2[i] == s2[j]:
            res2[len(res2)-1].append(s[j])
            if s[i] not in res:
                res.append(s2[i])
print(res2)


# 2 вариант, с практики
strsort = []
s = ["eat","tea","tan","ate","nat","bat"]
for word in s:
    strsort.append("".join(sorted(word)))

strdict = {}

for i in range(len(strsort)):
    if strdict.get(strsort[i]) == None:
        strdict[strsort[i]] = []

    strdict[strsort[i]].append(s[i])

print(strdict.values())
