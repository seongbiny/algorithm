
n = int(input()) # 컴퓨터의 수
k = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
arr = [[] for _ in range(n+1)]

for i in range(k):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0
visited = [0] * (n+1)

def dfs(v):
    global cnt
    visited[v] = 1
    #print(v, end=' ')
    for i in arr[v]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)

