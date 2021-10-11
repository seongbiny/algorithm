def dfs(x, y, i):
    global result

    if len(i) == 7:
        result.add(i)
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, i + arr[nx][ny])


T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]

    result = set()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for x in range(4):
        for y in range(4):
            dfs(x, y, arr[x][y])

    print(f'#{tc} {len(result)}')






















                    








