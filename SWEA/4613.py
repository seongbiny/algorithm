T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # n행 m열
    arr = [list(map(str, input())) for _ in range(N)]
    cnt = 0

    for i in range(M):
        # 첫째 줄 무조건 흰색
        if arr[0][i] != 'W':
            arr[0][i] = 'W'
            cnt += 1
        # 마지막 줄 무조건 빨간색
        if arr[N-1][i] != 'R':
            arr[N-1][i] = 'R'
            cnt += 1

    result = []
    for i in range(1, N-2): # 1, 2, 3
        for j in range(i, N-1): # i~4
            zz = 0
            for w in arr[1:i+1]:
                for x in w:
                    if x != 'W':
                        zz += 1
            for b in arr[i+1:j+1]:
                for y in b:
                    if y != 'B':
                        zz += 1
            for r in arr[j+1:N-1]:
                for z in r:
                    if z != 'R':
                        zz += 1
            result.append(zz+cnt)

    print(f'#{tc} {min(result)}')



