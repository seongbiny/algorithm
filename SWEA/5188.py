def dfs(x, y):
    global total, sub_sum

    if total < sub_sum:
        return

    if x == N-1 and y == N-1:
        total = sub_sum
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and [nx,ny] not in visited:
            visited.append((nx,ny))
            sub_sum += arr[nx][ny]
            dfs(nx,ny)
            visited.remove((nx,ny))
            sub_sum -= arr[nx][ny]

def solve(x,y,sub_sum):
    global total
    if sub_sum > total:
        return
    if x == N-1 and y == N-1:
        if sub_sum < total:
            total = sub_sum
            return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            solve(nx,ny,sub_sum+arr[nx][ny])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = N * N * 13
    sub_sum = arr[0][0]
    visited = []

    # 오른쪽이나 아래만 이동 가능
    dy = [0,1]
    dx = [1,0]

    #dfs(0,0)
    solve(0,0,sub_sum)

    print(f'#{tc} {total}')



