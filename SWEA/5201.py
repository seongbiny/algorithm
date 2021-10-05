T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    freight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    freight.sort(reverse=True)
    truck.sort(reverse=True)

    total = 0

    for i in range(N): # 0 1 2
        for j in range(M): # 0 1
            if freight[i] <= truck[j]:
                total += freight[i]
                freight[i] = 0
                truck[i] = 0

    print(f'#{tc} {total}')
