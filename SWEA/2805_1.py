T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    sumV = 0
    # N//2 보다 작은 곳
    for i in range(N//2): # 0 1 2
        for k in range(i+1): # 1 2 3
            if k == 0:
                sumV += arr[i][N//2]
            else:
                sumV += arr[i][N//2+k]
                sumV += arr[i][N//2-k]

    # N//2 인 곳
    for j in range(N):
        sumV += arr[N//2][j]

    # N//2 보다 큰 곳곳
    for i in range((N//2)+1, N): # 4 5 6
        for k in range(N-i): # 3 2 1
            if k == 0:
                sumV += arr[i][N//2]
            else:
                sumV += arr[i][N//2+k]
                sumV += arr[i][N//2-k]

    print(f'#{tc} {sumV}')