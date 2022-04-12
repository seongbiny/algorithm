import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y, )

h = []
high = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] not in h:
            h.append(arr[i][j])
            high = arr[i][j]

            visited = [[0] * n for _ in range(n)]
            cnt = 0

            for j in range(n):
                for k in range(n):
                    if arr[j][k] > high and visited[j][k] == 0:
                        bfs(j,k,high,visited)
                        cnt += 1