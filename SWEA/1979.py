# 01110
# 11100
# 00111
# 11101
# 10111

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 1 = 흰색, 0 = 검정
    # 흰색에 넣어야함
    # 1*k 의 양 옆에 0 이거나 벽이면 됨
    cnt = 0
    for i in range(n): # 0 1 2 3 4
        check = 0
        for j in range(n): # 0 1 2 3 4
            if arr[i][j] == 1:
                check += 1
            if arr[i][j] == 0 or j == n-1:
                # 벽을 만났을때 그동안 쌓아온 check 값이 k 이면 체크
                if check == k:
                    cnt += 1
                check = 0

        for j in range(n): # 0 1 2 3 4
            if arr[j][i] == 1:
                check += 1
            if arr[j][i] == 0 or j == n-1:
                if check == k:
                    cnt += 1
                check = 0

    print(f'#{tc} {cnt}')








