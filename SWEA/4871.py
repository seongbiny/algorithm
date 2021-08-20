def findW(v):
    for i in range(0, len(lst), 2):
        if v == lst[i] and visited[lst[i+1]]==False:
            return lst[i+1]
        if v == lst[i+1] and visited[lst[i]]==False:
            return lst[i]
    return -1

def dfs(v):
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

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    lst = []
    visited = [False] * (n-1)
    st = []
    for i in range(e):
        a, b = map(int, input().split())
        lst.append(a)
        lst.append(b)
    s, g = map(int, input().aplit())
# lst = [1, 4, 1, 3, 2, 3, 2, 5, 4, 6]



