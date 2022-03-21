import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
virus = []

dy = [1,0,-1,0]
dx = [0,1,0,-1]
def bfs(s, x, y):
    q = deque(virus)
    count = 0
    while q:
        if count == s:
            break
        for _ in range(len(q)):
            num, cur_x, cur_y = q.popleft()
            for k in range(4):
                nx = cur_x + dx[k]
                ny = cur_y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == 0:
                        arr[nx][ny] = arr[cur_x][cur_y]
                        q.append((arr[nx][ny], nx, ny))
        count += 1
    return arr[x-1][y-1]

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus.append((arr[i][j], i, j))

virus.sort()
print(bfs(s,x,y))

