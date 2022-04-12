'''
1. 2차원 배열을 처음부터 끝까지 돌면서 가장 높은 숫자를 뽑는다.
2. 0~가장높은숫자 까지 반복문으로 돌린다.
'''

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
high = 0

dy = [1,0,-1,0]
dx = [0,1,0,-1]
def bfs(y,x,high):
    q = deque()
    q.append((y,x))
    count = 1
    while q:
        y, x = q.popleft()
        visited[y][x] = 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<n and 0<=nx<n:
                if arr[ny][nx] > high and visited[ny][nx] == 0:
                    q.append((ny,nx))
                    visited[ny][nx] = 1
                    count += 1
    return count


for j in range(n):
    for i in range(n):
        high = max(high, arr[j][i])
# 배열을 돌면서 최고점을 뽑는다.

cnt = 0
for h in range(high): # 0 1 2 3... high-1
    visited = [[0]*n for _ in range(n)]
    result = []
    for j in range(n):
        for i in range(n):
            if arr[j][i] > h and visited[j][i] == 0:
                result.append(bfs(j,i,h))
    cnt = max(cnt, len(result))
print(cnt)
