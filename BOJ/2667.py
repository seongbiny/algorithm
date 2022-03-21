import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
house = [list(map(int, ' '.join(input()).split())) for _ in range(n)]
h_num = []

dy = [1,0,-1,0]
dx = [0,1,0,-1]
def bfs(x, y):
    count = 1
    q = deque()
    q.append((x,y))
    house[x][y] = 0
    while q:
        cur_x, cur_y = q.popleft()
        for k in range(4):
            nx = cur_x + dx[k]
            ny = cur_y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if house[nx][ny] == 1:
                    count += 1
                    q.append((nx,ny))
                    house[nx][ny] = 0
    return count

for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            h_num.append(bfs(i,j))
h_num.sort()
print(len(h_num))
for i in h_num:
    print(i)


