def dfs(x,y):
    global start_point, total
    if total < start_point:
        return
    if x == N-1 and y == N-1:
        total = start_point

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < N and ny < N and (nx, ny) not in visited:
            visited.append((nx,ny))
            start_point += arr[nx][ny]
            dfs(nx, ny)
            visited.remove((nx,ny))
            start_point -= arr[nx][ny]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1]
    dy = [1, 0]

    visited = []

    start_point = arr[0][0]
    total = N*N*13

    dfs(0,0)

    print(f'#{tc} {total}')