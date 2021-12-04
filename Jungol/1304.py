n = int(input())
arr = [[0]*n for _ in range(n)]
num = 1
for i in range(n):
    for j in range(n):
        arr[j][i] = num
        num += 1

for i in range(n):
    result = ''
    for j in range(n):
        result += str(arr[i][j]) + ' '
    print(result)
