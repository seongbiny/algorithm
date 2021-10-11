T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    check = N*N*[0]+[0]

    for i in range(N):
        for j in range(N):
            for d in range(4):
                start = room[i][j]
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if room[nx][ny] == start + 1:
                        check[start] += 1
    #print(check)
    i = N
    cnt = 1
    max_min = 0
    idx = 0
    while i >= 0:
        if check[i] == 1:
            cnt += 1
        else:
            if max_min <= cnt:
                max_min = cnt
                idx = i
            cnt = 1
        i -= 1
    print(f'#{tc} {idx+1} {max_min}')