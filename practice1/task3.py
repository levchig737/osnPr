from numpy import mat


matrix = [
[1,0,1,1,1],
[0,0,1,1,0],
[1,1,1,1,1],
]
N = len(matrix)
M = len(matrix[0])
maxn = 0

for i in range(N-1):
    for j in range(M-1):
        if matrix[i][j] > 0 and matrix[i+1][j] > 0 and matrix[i][j+1] > 0 and matrix[i+1][j+1] > 0:
            matrix[i+1][j+1] += 1
        if matrix[i][j] == matrix[i+1][j] == matrix[i][j+1] == matrix[i+1][j+1]:
            matrix[i+1][j+1] += 1
        if matrix[i+1][j+1] > maxn:
            maxn = matrix[i+1][j+1]


for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=" ")
    print()
print(maxn)