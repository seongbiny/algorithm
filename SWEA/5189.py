def dfs(x):
    global start_point, total, N
    if len(visited) == N:
        start_point += e[x][0]
        if total < start_point:
            start_point -= e[x][0]
            return

    if total < start_point:
        return
    elif len(visited) == N:
        total = start_point
        start_point -= e[x][0]
        return

    for i in range(1, N):
        if i not in visited:
            visited.append(i)
            start_point += e[x][i]
            dfs(i)
            visited.remove(i)
            start_point -= e[x][i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]

    visited = [0]

    start_point = 0
    total = 9999999

    for i in range(1, N):
        start_point += e[0][i]
        visited.append(i)
        dfs(i)
        visited.remove(i)
        start_point -= e[0][i]

    print(f'#{tc} {total}')

