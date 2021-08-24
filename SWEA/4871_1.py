def dfs(s, g):
    stack = [] # 빈 리스트 스택 만들기
    visited = [False] * (V+1) # 방문검사
    stack.append(s) # 스택에 시작점을 넣는다.

    # 스택이 전부 비워질때까지 반복문 돌리기
    while stack:
        # 스택에서 꺼내서 현재 값에 할당
        cur = stack.pop()
        # 현재 값 방문표시 해주기
        visited[cur] = True
        # 현재 값에 인접한 근처 간선을 살펴보기
        for w in range(1, V+1):
            # 방문은 하지 않았는데 인접하다면
            if not visited[w] and arr[cur][w]:
                # 갈 수 있으므로 스택에 push
                stack.append(w)
    # 돌다가 끝점에 도착
    if visited[g]:
        # 1 반환
        return 1
    else:
        return 0

T = int(input())

for tc in range(1, 1+T):
    V, E = map(int, input().split())
    arr = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1

    s, g = map(int, input().split())

    print(f'#{tc} {dfs(s, g)}')
