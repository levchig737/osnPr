nums = [3,1,4,2]

flag = False
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            if nums[i] < nums[k] < nums[j]:
                print(True)
                flag = True
                break
        if flag:
            break
    if flag:
        break

if not flag:
    print(False)