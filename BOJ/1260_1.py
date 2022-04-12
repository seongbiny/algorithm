import sys
input = sys.stdin.readline
from collections import deque

def dfs(v): # dfs는 스택 사용 / 재귀
    visited[v] = 1 # 방문처리 리스트 1개를 재사용하기위해 dfs는 1로처리
    print(v, end=" ")
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v): # bfs는 큐 사용 / 반복문
    q = deque()
    q.append(v)
    visited[v] = 0 # 방문처리 리스트 1개를 재사용하기위해 bfs는 0으로처리
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if visited[i] == 1 and graph[v][i] == 1: # 방문을 안했고 그래프 표시되어있으면
                q.append(i) # 큐에 넣어주고
                visited[i] = 0 # 방문처리 해준다.

n, m, V = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(V)
print()
bfs(V)