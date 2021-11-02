dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# def dfs(x, y):
#     global result
#
#     if arr[x][y] == 3:
#         result = 1
#         return
#
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if 0 <= nx < 100 and 0 <= ny < 100:
#             if visited[nx][ny] == 1 or arr[nx][ny] == 1:
#                 continue
#             else:
#                 visited[nx][ny] = 1
#                 dfs(nx, ny)

def bfs(x, y):
    global result
    q = [(si, sj)]
    arr[si][sj] = 1

    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if arr[nx][ny] == 0:
                q.append((nx, ny))
                arr[nx][ny] = 1
            elif arr[nx][ny] == 1:
                continue
            elif arr[nx][ny] == 3:
                result = 1
                return


for _ in range(10):
    tc = input()
    arr = [list(map(int, input())) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]
    si, sj = 0, 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                si, sj = i, j

    result = 0
    # dfs(si, sj)
    bfs(si, sj)
    print(f'#{tc} {result}')