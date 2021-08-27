import sys
sys.stdin = open("input_1974.txt","r")

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    cnt = 1

    for i in range(9): # 0 1 2 3 4 5 6 7 8
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9): # 0 1 2 3 4 5 6 7 8
            if arr[i][j] in num:
                num.remove(arr[i][j])
            elif arr[i][j] not in num:
                cnt = 0
                break

    for i in range(9): # 0 1 2 3 4 5 6 7 8
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9): # 0 1 2 3 4 5 6 7 8
            if arr[j][i] in num:
                num.remove(arr[j][i])
            elif arr[j][i] not in num:
                cnt = 0
                break

    for i in [0, 3, 6]: # 0 3 6
        for j in [0, 3, 6]: # 0 3 6
            num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if arr[x][y] in num:
                        num.remove(arr[x][y])
                    elif arr[x][y] not in num:
                        cnt = 0
                        break

    if cnt == 1:
        print(f'#{tc} {cnt}')
    else:
        print(f'#{tc} {cnt}')






