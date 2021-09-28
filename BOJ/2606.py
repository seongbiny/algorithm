n = int(input()) # 컴퓨터의 수
m = int(input()) # 간선의 수
matrix = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

linked = [0] * (n+1)

cnt = 0
def dfs(v):
    global cnt
    linked[v] = 1
    for i in range(1, n+1):
        if linked[i] == 0 and matrix[v][i] == 1:
            cnt += 1
            dfs(i)
    return cnt

def bfs(v):
    global cnt
    queue = [v]
    linked[v] = 1
    while queue:
        v = queue.pop(0)
        for i in range(1, n+1):
            if linked[i] == 0 and matrix[v][i] == 1:
                queue.append(i)
                linked[i] = 1
                cnt += 1
    return cnt

print(bfs(1))