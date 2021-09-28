N, M, V = map(int, input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visited = [0] * (N+1)

def dfs(V):
    visited[V] = 1 # 방문한 점 1로 체크
    print(V, end=' ')
    for i in range(1, N+1):
        if visited[i] == 0 and matrix[V][i] == 1:
            dfs(i)

def bfs(V):
    queue = [V] # 들려야 할 정점 저장
    visited[V] = 0 # 방문한 점 0으로 체크
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if visited[i] == 1 and matrix[V][i] == 1:
                queue.append(i)
                visited[i] = 0

dfs(V)
print()
bfs(V)
