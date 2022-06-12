def search_sum(amount, res=[]):
    global s
    for n in nums:
        p = amount - n
        if p == 0:
            res.append(str(n))
            s.add("+".join(sorted(res)))
        elif p > 0:
            search_sum(p, res+[str(n)])
        

amount = 23
nums = [3,5,4,13]
s = set()

search_sum(amount)

if len(s) == 0:
    s.add('0')

print(s)