def dfs(v):
    st = []
    visited = [False] * 8
    st.append(v)
    visited[v] = True
    while st:
        v = st.pop(-1)
        print(v)
        for w in G[v]:
            if not visited[w]:
                st.append(w)
                visited[w] = True

def bfs_G(v):
    Q = []
    visited = [False] * 8
    Q.append(v)
    visited[v] = True
    while Q:
        v = Q.pop(0)
        print(v)
        for w in G[v]:
            if not visited[w]: # 방문표시 안한것
                Q.append(w)
                visited[w] = True


def bfs_adj(v):
    Q = []
    visited = [False] * 8
    Q.append(v)
    visited[v] = True
    while Q:
        v = Q.pop(0)
        print(v)
        for w in range(len(adj[v])):
            if adj[v][w] == 1 and not visited[w]:
                Q.append(w)
                visited[w] = True

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = [[] for _ in range(8)]
adj = [[0] * 8 for _ in range(8)]
#print(G)
for i in range(0, 16, 2):
    v1 = lst[i]
    v2 = lst[i+1]

    G[v1].append(v2)
    G[v2].append(v1)
    adj[v1][v2] = 1
    adj[v2][v1] = 1

#bfs_G(1)
#bfs_adj(1)
dfs(1)