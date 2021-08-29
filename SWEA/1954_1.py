

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    mode = 0

    x = y = 0
    arr[x][y] = 1

    for num in range(2, n**2+1):
        x = x + dx[mode]
        y = y + dy[mode]
        arr[x][y] = num

        if 0<= x + dx[mode] <n and 0<= y + dy[mode] <n and not arr[x + dx[mode]][y + dy[mode]]:
            continue

        if mode != 3:
            mode += 1
        else:
            mode = 0

    print(f'#{tc}')
    for i in arr:
        print(*i)
