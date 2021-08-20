
def dfs(v):
    st = []
    visited = [False] * (V+1)

    st.append(v) # 첫번재 점을 무조건 스택에 한번 넣는다
    #스택에 넣을때 방문 표시를 해준다
    visited[v] = True

    while st: # st에 데이터가 있는 동안 반복 아무것도 없으면 돌아가지않으니까 처음 지점을 넣어주는 것
        v = st.pop(-1) # 스택에 하나 팝 해서 인접한 애랑
                                   # 처리 할 땐 여기서
        #print(v)
        if v == G:
            return 1
        for w in GR[v]:            #인접했다
            if visited[w] == False:
                st.append(w) #스택에 넣을때 무조건 방문표시해줘라 그래야 두번 안들어가니까
                visited[w] = True
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    #GR = [0] * (V+1) append 말고 = 1 이런식으로 ~
    GR = [[] for _ in range(V+1)]

    for i in range(E):
        v1, v2 = map(int, input().split())
        GR[v1].append(v2)
        #GR[v2].append(v1) 방향 그래프가 아니라면 이것도 적어야함

    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S)}')
