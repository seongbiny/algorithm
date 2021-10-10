def solve(x, y, sumV):
    global total
    if sumV > total:
        return
    if x == N-1 and y == N-1:
        if sumV < total:
            total = sumV
        return

    if x+1 < N:
        solve(x+1, y, sumV+arr[x+1][y])
    if y+1 < N:
        solve(x, y+1, sumV+arr[x][y+1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = N*N*13
    solve(0,0,arr[0][0])

    print(f'#{tc} {total}')


