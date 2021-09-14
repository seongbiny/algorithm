T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())
    arr = [[0]*300 for _ in range(300)]

    x_1, x_2, y_1, y_2 = 0, 0, 0, 0

    num = 1
    for i in range(1, 300):
        x, y = 1, i
        for j in range(i):
            arr[x][y] = num
            num += 1
            x += 1
            y -= 1

    # print(arr)  대각선으로 수를 채움
    # 5 -> (2,2)  1 -> (1,1)

    for x in range(1, 300):
        for y in range(1, 300):
            if p == arr[x][y]:
                x_1 = x
                y_1 = y
            if q == arr[x][y]:
                x_2 = x
                y_2 = y

    new_x = x_1 + x_2
    new_y = y_1 + y_2

    for x in range(1, 300):
        for y in range(1, 300):
            new = arr[new_x][new_y]

    print(f'#{tc} {new}')



