t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# bfs를 통한 탐색
def dfs(x, y):
    global ans, ex, ey, cnt
    # 방문표시
    if x == ex and y == ey:
        cnt += 1
        ans = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 범위안에 있고 길이 0이면 방문표시 후 탐색
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and (arr[nx][ny] == 0 or arr[nx][ny] == 3):
            visited[nx][ny] = 1
            dfs(nx, ny)
            visited[nx][ny] = 0
    # 엔드지점 도달 못했으면 ans= 0 저장


for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    cnt = 0
    ans = 0
    # 시작지점, 엔드지점 찾아주기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                sx = i
                sy = j
            if arr[i][j] == 3:
                ex = i
                ey = j
    dfs(sx, sy)
    if ans == 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} {ans} {cnt}')
    # print(f'#{tc} {ans}')
