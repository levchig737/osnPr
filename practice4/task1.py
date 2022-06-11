nums = [-2,1,-3,4,-1,2,1,-5,4]
summ = 0
maxs = max(nums)

for i in nums:
    summ += i

    if maxs < summ:
        maxs = summ

    if (summ) <= 0:
        summ = 0

print(maxs)