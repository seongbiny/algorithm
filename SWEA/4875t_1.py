# dfs 문제이다 !!!

def dfs_o(v):
    st.append(v)
    visited[v] = True

    while st:
        v = st.pop()
        print(v) # 여기서 처리해줘라
        for w in G[v]: #인접한 w들
            if not visited[w]: #== False:
                st.append(w)
                visited[w]


def dfs(curx, cury):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    st = []
    # 시작지점에서 종료지점까지 갈 수 있으면 1을 return
    # 아니면 0을 return

    st.append((curx, cury))
    arr[cury][curx] = 1 # 방문처리 하는거 벽으로 인식하게끔

    while st:
        (curx, cury) = st.pop()
        # if arr[curx][cury] == 3:
        #     return 1

        #print(...) 처리 하는 부분
        for d in range(4):
            newx = curx + dx[d]
            newy = cury + dy[d]
            # if 0 <= newy < n and 0 <= newx < n and arr[newx][newy] == 3:
            #     return 1bfs

            if 0 <= newy < n and 0 <= newx < n and arr[newx][newy] != 1: # 이면 갈 수 있다 3일때도 처리해줘야함
                if arr[newy][newx] == 3:
                    return 1
                st.append((newx, newy))
                arr[newy][newx] = 1
    return 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    #arr = [list(map(int, input())) for _ in range(n)]
    arr = [list(int(input())) for _ in range(n)]
    #arr = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                curx = j
                cury = i
                break

    result = dfs(curx, cury)
    print(f'#{tc} {result}')



