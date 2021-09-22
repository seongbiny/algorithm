from collections import deque

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

# 너비 우선 탐색
def bfs(start_v):
    visited = [start_v]
    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in range(len(graph[start_v])):
            if graph[v][w] == 1 and (w not in visited):
                visited.append(w)
                queue.append(w)

# 깊이 우선 탐색
def dfs(start_v, visited=[]):
    visited.append(start_v)
    print(start_v, end=' ')

    for w in range(len(graph[start_v])):
        if graph[start_v][w] == 1 and (w not in visited):
            dfs(w, visited)

dfs(v)
print()
bfs(v)


