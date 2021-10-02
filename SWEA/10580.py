T = int(input())
for tc in range(1, T+1):
    n = int(input())
    line = [[] for _ in range(n)]
    cross = 0
    for i in range(n):
        line[i] = list(map(int, input().split()))

    for j in range(n-1): # 0, 1
        for k in range(j+1, n): # 1, 2 // 2
            left_1 = line[j][0]
            right_1 = line[j][1]
            left_2 = line[k][0]
            right_2 = line[k][1]

            if (left_1 > left_2 and right_1 < right_2) or (left_1 < left_2 and right_1 > right_2):
                cross += 1

    print(f'#{tc} {cross}')

