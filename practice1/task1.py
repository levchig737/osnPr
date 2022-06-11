from pickle import NEXT_BUFFER

from numpy import number


numbers = [4,-1,7,0,1,2,-1,5]
lenght = len(numbers)

for i in range(lenght):
    for j in range(i+1, lenght):
        for k in range(j+1, lenght-1):
            if numbers[i] + numbers[j] + numbers[k] == 0:
                print(numbers[i], numbers[j], numbers[k])