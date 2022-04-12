import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    m, n, k = map(int,input().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int,input().split())
        arr[b][a] = 1

    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    def bfs(y,x):
        q = deque()
        q.append((y,x))
        arr[y][x] = 0
        while q:
            y, x = q.popleft()
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0<=ny<n and 0<=nx<m and arr[ny][nx] == 1:
                    arr[ny][nx] = 0
                    q.append((ny,nx))

    cnt = 0
    for j in range(n):
        for i in range(m):
            if arr[j][i] == 1:
                bfs(j,i)
                cnt += 1
    print(cnt)
