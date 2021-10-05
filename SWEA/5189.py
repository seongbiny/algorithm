def dfs(cur, sub_sum):
    global total
    if sub_sum < total:
        if 0 not in visited[1:]:
            total = min(total, sub_sum + e[cur][0])
            return
        for j in range(1, N):
            if e[cur][j] != 0 and visited[j] == 0:
                visited[j] = 1
                dfs(j, sub_sum+e[cur][j])
                visited[j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    e = [list(map(int,input().split())) for _ in range(N)]

    total = 99999

    for i in range(1, N): # 1 2
        visited = [0] * N # [0, 0, 0]
        visited[i] = 1
        dfs(i, e[0][i])
    print(f'#{tc} {total}')


