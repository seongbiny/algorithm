'''
맵을 탐색하면서 양이거나 늑대면 bfs 함수 호출
울타리 내에서 양과 늑대의 수를 센다.
'''

import sys
input = sys.stdin.readline

r, c = map(int,input().split())
map = [list(map(str, ' '.join(input()).split())) for _ in range(r)]

dy = [1,0,-1,0]
dx = [0,1,0,-1]
def bfs(y, x):
    q = [(y,x)]
    o = 0
    v = 0
    while q:
        cur_y, cur_x = q.pop()
        if map[cur_y][cur_x] == 'v':
            v += 1
        elif map[cur_y][cur_x] == 'o':
            o += 1
        map[cur_y][cur_x] = '#'
        # 방문한 곳을 '#'으로 만들어서 방문체크 함

        for k in range(4):
            ny = cur_y + dy[k]
            nx = cur_x + dx[k]
            if 0<=ny<r and 0<=nx<c:
                if map[ny][nx] != '#':
                    q.append((ny,nx))
    if o <= v:
        o = 0
    else:
        v = 0
    return o, v

o_num = 0
v_num = 0
for j in range(r):
    for i in range(c):
        if map[j][i] == 'v' or map[j][i] == 'o':
            o, v = bfs(j,i)
            o_num += o
            v_num += v

print(o_num, v_num)