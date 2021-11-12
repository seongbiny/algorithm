T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    result = [0] * N


    for b in range(M): # 0 1 2
        for a in range(N): # 0 1 2 3
            if alist[a] <= blist[b]:
                result[a] += 1
                break

    maxV = 0
    idx = 0
    for i in range(N):
        if result[i] > maxV:
            maxV = result[i]
            idx = i+1

    print(f'#{tc} {idx}')