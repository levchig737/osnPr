nums = [4,-1,7,0,1,2,-1,5] 
S = 3

for i in range(len(nums)-1):
    summ = nums[i]
    res = [nums[i]]
    for j in range(i+1,len(nums)-1):
        summ += nums[j]
        res.append(nums[j])
        if summ > S:
            break
        if summ == S:
            print(res)
            break