import sys
sys.stdin = open("input_1219.txt","r")

def dfs(v): # v는 시작점
    visited[v] = True # visited 체크하기 1로 체크
    # print(v, end=' ')
    # 시작정점(v)의 인접한 모든 점정(w)에 for 돌리기
    # 인접정점(w)가 방문하지 않았으면
    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w) # 다시 dfs(w) 재귀 호출

for _ in range(10):

    V = 100
    tc, E = map(int, input().split()) # V: 정점개수, E: 간선개수
    # print(tc, E)
    arr = list(map(int, input().split())) # 2차원 리스트 데이터 받기
    # print(tmp)
    adj = [[0] * (V+1) for _ in range(V+1)] # 인접행렬 초기화
    visited = [0] * (V+1) # 방문행렬

    # 입력
    for i in range(E):
        s, e = arr[2*i], arr[2*i+1] # s 시작점, e 마지막점
        adj[s][e] = 1

    #for i in range(0, len(arr), 2):

    # for i in range(V+1):
    #     print(f'{i} {adj[i]})

    print(f'#{tc}', end=' ')
    dfs(0) # A 도시
    if visited[99] == True:
        print(1)
    else:
        print(0)