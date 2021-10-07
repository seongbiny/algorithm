def dfs(i, max_i, cnt):
    global res
    if cnt >= res:
        return
    if max_i >= N:
        res = min(cnt, res)
        return
    for j in range(max_i, i, -1):
        dfs(j, j + M[j], cnt + 1)


T = int(input())
for tc in range(1, T+1):
    tmp = list(map(int, input().split()))
    N = tmp[0]
    M = [0] + tmp[1:]

    res = 10000
    dfs(1, 1+M[1], 0)
    print(f'#{tc} {res}')