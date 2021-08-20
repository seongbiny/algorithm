lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
g = {0:[], 1:[2, 3], 2:[1, 4, 5], 3:[1, 7], 4:[2, 6], 5:[2, 6], 6:[4, 5, 7], 7:[3, 6]}
# a,b,c,d,... 일때 사용하면 편하다
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0]
       ]
#v에 인접한 정점 중 방문하지 않은 정점을 하나 찾아서 return 한다
#방문하지 않은 정점이 없으면 -1을 return한다
def findW1(v):
    for i in range(0, len(lst), 2):
        if v == lst[i] and visited[lst[i+1]]==False:
            return lst[i+1]
        if v == lst[i+1] and visited[lst[i]]==False:
            return lst[i]
    return -1

def findW2(v):
    for w in g[v]:
        if visited[w] == False:
            return w
    return -1

def findW(v):
    for i in range(len(adj[v])):
        if adj[v][i]==1 and visited[i] == False:
            return i
    return -1

n = 7
visited = [False] * (n+1) #0번(비워놓는다) ~ 7번 까지 방문 안한 상태
st = []

def dfs(v): # 시작점을 받아서 방문을 한다
    visited[v] = True
    print(v)
    st.append(v)
    while st:    #len(st) > 0:
        w = findW(v) #정점 w를 찾는 함수
        if w != -1:
            st.append(v)
            visited[w] = True
            print(w)
            v = w
        else:
            v = st.pop(-1)


dfs(1)

