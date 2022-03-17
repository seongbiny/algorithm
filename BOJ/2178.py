import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, ' '.join(input()).split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
# print(arr)
dy = [1,0,-1,0]
dx = [0,1,0,-1]
def bfs(y, x):
    cnt = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] == 1 and chk[ny][nx] == False:
                    cnt += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return cnt

minv = 100000

for j in range(n):
    for i in range(m):
        if arr[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            minv = min(minv, bfs(j,i))

print(minv)
