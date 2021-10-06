N, M = map(int, input().split())
graph = [list(map(int,input())) for _ in range(N)]

def dfs(x, y):
    if 0 <= x < N and 0 <= y < M:
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1)
            return True
    return False

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            cnt += 1
print(cnt)