'''
bfs는 queue를 사용한다.
bfs는 현재 노드에서 가까운 곳부터 찾기 때문에 경로 탐색 시 첫번재로 찾아가는 길이 최단거리이다.
'''

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, ' '.join(input()).split())) for _ in range(n)]

dy = [1,0,-1,0]
dx = [0,1,0,-1]
def bfs(y,x):
    q = deque()
    q.append((y,x))
    while q:
        cur_y, cur_x = q.popleft()
        for k in range(4):
            new_y = cur_y + dy[k]
            new_x = cur_x + dx[k]
            if 0<= new_y < n and 0<= new_x < m and arr[new_y][new_x] == 1:
                arr[new_y][new_x] = arr[cur_y][cur_x] + 1
                q.append((new_y,new_x))
    return arr[n-1][m-1]

print(bfs(0,0))
# print(arr)

'''
[[3, 0, 9, 10, 11, 12], 
[2, 0, 8, 0, 12, 0], 
[3, 0, 7, 0, 13, 14], 
[4, 5, 6, 0, 14, 15]]

[[3, 2, 0, 8, 9, 0], 
[2, 3, 0, 7, 8, 0], 
[3, 4, 5, 6, 7, 8], 
[4, 5, 6, 7, 0, 9]]
'''