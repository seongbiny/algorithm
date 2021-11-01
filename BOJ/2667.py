import sys import stdin
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, c):
    visited[x][y] = 1
    global house
    if arr[x][y] == 1:
        house += 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                dfs(nx, ny, c)

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
for i in range(N):
    line = stdin.readline().strip()
    for j, b

house = 0
cnt = 1
lst = []
# 조사 할 첫 가구 정하기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            dfs(i, j, cnt)
            lst.append(house)
            house = 0

print(len(lst))
for i in sorted(lst):
    print(i)