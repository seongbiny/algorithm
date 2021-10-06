# 퀸은 같은 행,열,대각선에 놓일수없다 -> 행 열 대각선 체크
def dfs(idx): # 행 넣음
    global N, cnt
    if idx == N: # 모든 행을 체크하면 + 1
        cnt += 1
        return

    check = 0
    for i in range(N): # 열 체크
        if col[i] == 0:
            for x, y in queen:
                if abs(idx-x) == abs(i-y): # 행과 열의 차이가 같으면 대각선에 있는거
                    check = 1
                    break

            if check != 1:
                col[i] = 1
                queen.append((idx, i))
                #print(queen)
                dfs(idx+1)
                col[i] = 0
                queen.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    col = [0] * N
    queen = []
    dfs(0)
    print(f'#{tc} {cnt}')


