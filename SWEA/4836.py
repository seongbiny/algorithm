T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]
    cnt = 0
    for k in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if arr[i][j] == 0:
                        arr[i][j] = color
                    elif arr[i][j] == 2:
                        cnt += 1
        elif color == 2:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if arr[i][j] == 0:
                        arr[i][j] = color
                    elif arr[i][j] == 1:
                        cnt += 1

    print(f'#{tc} {cnt}')







