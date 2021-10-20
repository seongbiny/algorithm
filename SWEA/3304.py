T = int(input())
for tc in range(1, T+1):
    a, b = map(str, input().split())
    a = list(a)
    b = list(b)

    arr = [[0]*(len(a)+2) for _ in range(len(b)+2)]

    for i in range(2, len(a)+2):
        arr[0][i] = a[i-2]
    for i in range(2, len(b)+2):
        arr[i][0] = b[i-2]

    maxv = 0
    for i in range(2, len(b)+2):
        for j in range(2, len(a)+2):
            if arr[0][j] == arr[i][0]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
                if arr[i][j] > maxv:
                    maxv = arr[i][j]

    print(f'#{tc} {maxv}')


