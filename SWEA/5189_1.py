def battery(cnt, y, total):
    global result
    if cnt == N:
        total += arr[y][0]
        if total < result:
            result = total
            return
    if total > result:
        return
    for i in range(1, N):
        if not arr[y][i]:
            continue
        if not visited[i]:
            visited[i] = 1
            battery(cnt+1, i, total+arr[y][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = 100 * N
    battery(1,0,0)
    print(f'#{tc} {result}')