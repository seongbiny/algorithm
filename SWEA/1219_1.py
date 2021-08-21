import sys
sys.stdin = open("input_1219.txt","r")

for _ in range(1):
    tc, n = map(int, input().split())
    road = list(map(input().split()))

    # 1. 홀짝
    # 2. 2step
    # 3. 2*?

    # or i in range(n):
    #    st = road[2*i]
    #    ed = road[2*i+1]

    #########################
    # 저장 방법
    # 1. ch1, ch2
    # ch1 = [0] * 100
    # ch2 = [0] * 100
    #
    # for i in range(n):
    #     if ch1[road[2*i]] == 0:
    #         ch1[road[2*i]] = road[2*i+1]
    #     else:
    #         ch2[road[2*i]] = road[2*i+1]  #ch1,ch2 안나누고 ch 로 2차원배열 받아도 돼
    # # 인접행렬 = 각각의 정점을 2차원리스트로 만들어서 연결상태를 표시
    # # 2. 인접행렬 방식
    # adj_arr = [[0] *100 for _ in range(100)]
    # for i in range(n):
    #     adj_arr[road[2*i]][road[2*i+1]] = 1

    # 3. 인접리스트 방식
    # adj_list = [[] for _ in range(100)]
    # for i in range(n):
    #     adj_list[road[2*i]].append(road[2*i+1])
    #
    # visited = [0] * 100
    # ans = 0
    #
    # stack = [0]
    #
    # while stack: #len(stack) > 0
    #     curr = stack.pop()
    #
    #     if curr == 99:
    #         ans = 1
    #         break
    #     #방문하지 않았으면
    #
    #     #방문을 했으면 건너가
    #     if visited[curr]: continue #밑에적은 코드 실행할 필요없고 넘어가
    #     visited[curr] = 1
    #
    #     for w in adj_list[curr]:
    #         if not visited[w]:
    #             stack.append(w)
    #
    #     print(f'#{tc} {ans}')

    ##############################################

def dfs(v):
    if v == 99:
        ans = 1
        return
    visited[v] = 1
    for w in range(100):
        if not visited[w] and adj_arr[v][w]:
            dfs(w)

for _ in range(1):
    tc, n = map(int, input().split())
    road = list(map(input().split()))

    adj_arr = [[0] * 100 for _ in range(100)]

    for i in range(n):
        adj_arr[road[2*i]][road[2*i+1]] = 1

    visited = [0] * 100
    ans = 0


