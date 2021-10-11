def dfs(x):
    global total, result
    if x == N:
        if total < result:
            result = total
            return
    if result <= total:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            total += arr[x][i]
            dfs(x+1)
            visited[i] = 0
            total -= arr[x][i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    total = 0
    result = 999999

    dfs(0)

    print(f'#{tc} {result}')