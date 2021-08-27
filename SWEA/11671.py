dx_1 = [-1, 1, 0, 0]
dy_1 = [0, 0, 1, -1]

dx_2 = [-1, 1, 0, 0, -2, 2, 0, 0]
dy_2 = [0, 0, 1, -1, 0, 0, 2, -2]

dx_3 = [-1, 1, 0, 0, -2, 2, 0, 0, -3, 3, 0, 0]
dy_3 = [0, 0, 1, -1, 0, 0, 2, -2, 0, 0, 3, -3]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if arr[x][y] == 'A':
                for i in range(4):
                    newx = x + dx_1[i]
                    newy = y + dy_1[i]
                    if 0 <= newx < n and 0 <= newy < n and arr[newx][newy] == 'H':
                        arr[newx][newy] = 'X'
            elif arr[x][y] == 'B':
                for i in range(8):
                    newx = x + dx_2[i]
                    newy = y + dy_2[i]
                    if 0 <= newx < n and 0 <= newy < n and arr[newx][newy] == 'H':
                        arr[newx][newy] = 'X'
            elif arr[x][y] == 'C':
                for i in range(12):
                    newx = x + dx_3[i]
                    newy = y + dy_3[i]
                    if 0 <= newx < n and 0 <= newy < n and arr[newx][newy] == 'H':
                        arr[newx][newy] = 'X'
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')
