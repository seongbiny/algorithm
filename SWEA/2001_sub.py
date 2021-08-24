T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    lst = []

    for i in range(n-m+1): # 0 1 2 3
        for j in range(n-m+1): # 0 1 2 3
            sumV = 0
            for row in range(m): # 0 1
                for col in range(m): # 0 1
                    sumV += arr[i + row][j + col]
            lst.append(sumV)

    print(f'#{tc} {max(lst)}')
