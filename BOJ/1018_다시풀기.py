n, m = map(int, input().split())
arr = [[] for _ in range(n)]

for l in range(n):
    arr[l] = list(input())

cnt = 0

for i in range(n): # 0 1 2 3 4 5 6 7
    for j in range(1, m, 2): # 1, 3, 5, 7
        if arr[i][0] == 'W':
            if arr[i][j] != 'B':
                cnt += 1
        else:
            if arr[i][j] != 'W':
                cnt += 1

    for k in range(2, m, 2): # 2, 4, 6
        if arr[i][0] == 'B':
            if arr[i][k] != 'B':
                cnt += 1
        else:
            if arr[i][k] != ' W':
                cnt += 1

print(cnt)