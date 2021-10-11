# 어차피 다음 방 번호가 현재 방 번호+1 이어야 움직일 수 있다는 조건이 있으므로
# 중복되는 경로가 없다. => visited 필요없음

def dfs(room[x][y], idx):
    global cnt
    if idx < cnt:
        return

    if x == N-1 and y == N-1:

        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if room[x][y] + 1 == room[nx][ny]:
                idx += 1
                dfs(room[nx][ny], idx)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for x in range(N):
        for y in range(N):
            dfs(room[x][y], idx)

    print(f'#{tc} {room[x][y]} {idx}')