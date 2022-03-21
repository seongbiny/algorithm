import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

queue = deque()

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for j in range(n):
    for i in range(m):
        if box[j][i] == 1:
            queue.append((j, i)) # 익어있는 토마토를 큐에 먼저 넣고 시작한다.

day = -1
while queue:
    day += 1
    for i in range(len(queue)): # 현재 익어있는 토마토만큼 반복문 돌린다.
        y,x = queue.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<n and 0<=nx<m and box[ny][nx]==0:
                box[ny][nx] = box[y][x]+1 # 토마토가 새로 익고
                queue.append((ny,nx)) # 익은 토마토 큐에 넣어준다
for i in box:
    if 0 in i:
        print(-1)
        break
else:
    print(day)