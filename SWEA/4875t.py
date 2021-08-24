# dfs 문제이다 !!!

def dfs(v):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    st = [] # 스타트 지점을 스택에 넣음
    st.append((curx, cury))
    # 방문은 첫번째방법 2차원 배열, 두번째 방법은 길을 벽으로 바꾼다.
    #visited[v] = True
    arr[cury][curx] = 1

    while st:
        v = st.pop()
        print(v)
        for d in range(4):
            newx = curx + dx[d]
            newy = cury + dy[d]
            if newx, newy: #를 이용해서 갈 수 있는 길이면(방문안했고) 범위체크, 0인지도 체크, 3일때 처리
                st.append((newx, newy))
                arr[newy][newx] = 1


curx, cury = 스타트 지점을 찾아서
dfs(curx, cury)

