check_x = [0, 0, 2, -2]
check_y = [-2, 2, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # 한 변의 길이 , 돌을 놓는 횟수
    arr = [[0] * N for _ in range(N)]
    for i in range(M):
        a, b, color = map(int, input().split())
        # 1 백돌 2 흑돌
        x, y = a-1, b-1
        if 0 <= x < N and 0 <= y < N:
            arr[x][y] = color

        for c in range(4):
            cx = x + check_x[c]
            cy = y + check_y[c]
            if 0 <= cx < N and 0 <= cy < N:
                if arr[cx][cy] == color:
                    if x != cx:
                        arr[abs(x-cx)][y] = color
                    elif y != cy:
                        arr[x][abs(y-cy)] = color
                    break
    print(arr)