import sys
sys.setrecursionlimit(10**9) # 재귀 함수의 최대깊이 늘려주는거

N = int(input()) # 노드의 개수
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

# 부모저장
parents = [0 for _ in range(N+1)]

def dfs(start, tree, parents):
    for i in tree[start]: # 연결된 노드 모두 탐색
        if parents[i] == 0: # 한번도 방문한 적이 없다면
            parents[i] = start # 부모 노드 저장
            dfs(i, tree, parents)

dfs(1, tree, parents)

for i in range(2, N+1):
    print(parents[i])


