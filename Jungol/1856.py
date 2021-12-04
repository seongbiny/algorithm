n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
num = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            arr[i][j] = num
            num += 1
    else:
        for j in range(m-1, -1, -1):
            arr[i][j] = num
            num += 1

for i in range(n):
    result = ''
    for j in range(m):
        result += str(arr[i][j]) + ' '
    print(result)


