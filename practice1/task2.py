nums = [4,-1,7,0,1,2,-1,5]
k = 3

def f(summ, nums):
    res = []
    for i in range(len(nums)):
        summ -= nums[i]
        res.append(nums[i])

        if summ == 0:
            return res

    return False


count = 0
for i in range(len(nums)):
    answer = f(k, nums[i:])
    if answer != False:
        count += 1
        print(answer)
    
print(count)