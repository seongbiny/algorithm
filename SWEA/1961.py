T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(str, input().split())) for _ in range(n)]
    # print(arr)
    arr_90 = [[0] * n for _ in range(n)]
    arr_180 = [[0] * n for _ in range(n)]
    arr_270 = [[0] * n for _ in range(n)]
    # 90 도 회전
    # 00 - 02 / 01 - 12 / 02 - 22
    # 10 - 01 / 11 - 11 / 12 - 21
    # 20 - 00 / 21 - 10 / 22 - 20
    for i in range(len(arr)):
        for j in range(n):
            arr_90[j][n - 1 - i] = arr[i][j]
    # print(arr_90)

    for i in range(len(arr_90)):
        for j in range(n):
            arr_180[j][n - 1 - i] = arr_90[i][j]
    # print(arr_180)

    for i in range(len(arr_180)):
        for j in range(n):
            arr_270[j][n - 1 - i] = arr_180[i][j]
    # print(arr_270)

    # arr_90[0], arr_90[1], arr_90[2] 안에 원소들 다 붙이고 00 10 20 으로
    # arr_180[0], arr_180[1], arr_180[2] 안에 원소들 다 붙이고 01 11 21
    # arr_270[0], arr_270[1], arr_270[2] 안에 원소들 다 붙이고 02 12 22
    new_90 = 0
    new_180 = 0
    new_270 = 0
    print(f'#{tc} ')
    for i in range(len(arr)):
        new_90 = ''.join(arr_90[i])
        new_180 = ''.join(arr_180[i])
        new_270 = ''.join(arr_270[i])
        print(new_90, new_180, new_270)