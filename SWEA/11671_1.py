drow1 = [-1, 1, 0, 0] # 상하좌우
dcol1 = [0, 0, 1, -1]


drow2 = [-1, 1, 0, 0, -2, 2, 0, 0] # 상하좌우
dcol2 = [0, 0, 1, -1, 0, 0, 2, -2]

drow3 = [-1, 1, 0, 0, -2, 2, 0, 0, -3, 3, 0, 0] # 상하좌우
dcol3 = [0, 0, 1, -1, 0, 0, 2, -2, 0, 0, 3, -3]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if arr[row][col] == 'A':
                for i in range(4):
                    newr = row + drow1[i]
                    newc = col + dcol1[i]
                    if 0 <= newr < n and 0 <= newc < n and arr[newr][newc] == 'H':
                        arr[newr][newc] = 'X'
            elif arr[row][col] == 'B':
                for i in range(8):
                    newr = row + drow2[i]
                    newc = col + dcol2[i]
                    if 0 <= newr < n and 0 <= newc < n and arr[newr][newc] == 'H':
                        arr[newr][newc] = 'X'
            elif arr[row][col] == 'C':
                for i in range(12):
                    newr = row + drow3[i]
                    newc = col + dcol3[i]
                    if 0 <= newr < n and 0 <= newc < n and arr[newr][newc] == 'H':
                        arr[newr][newc] = 'X'
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')