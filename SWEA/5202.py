T = int(input())

for tc in range(1, T+1):
    N = int(input())
    time = []
    for i in range(N):
        s, e = map(int,input().split())
        t = []
        t.append(e)
        t.append(s)
        time.append(t)

    time_list = sorted(time)
    # [[14, 4], [18, 8], [20, 17], [23, 20], [24, 23]]
    cnt = 0
    end_time = 0
    for i in range(N):
        end = time_list[i][0]
        start = time_list[i][1]
        if end_time <= start:
            cnt += 1
            end_time = end

    print(f'#{tc} {cnt}')