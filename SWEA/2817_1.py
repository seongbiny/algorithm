T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    lst = []
    result = 0
    cnt = 0
    for i in range(1<<N):
        for j in range(N+1):
            if i & (1 << j):
                result += A[j]
        #         print(A[j], end=' ')
        # print()
        if result == K:
            cnt += 1
        result = 0

    print(f'#{tc} {cnt}')