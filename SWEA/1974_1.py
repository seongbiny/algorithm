import sys
sys.stdin = open("input_1974.txt","r")

def row_check(arr):
    cnt = 0
    for i in range(9):
        if cnt != 0:
            return 0
        elif cnt == 0:
            num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if arr[i][j] in num:
                num.remove(arr[i][j])
            elif arr[i][j] not in num:
                cnt += 1
    return 1

def col_check(arr):
    cnt = 0
    for j in range(9):
        if cnt != 0:
            return 0
        elif cnt == 0:
            num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            if arr[i][j] in num:
                num.remove(arr[i][j])
            elif arr[i][j] not in num:
                cnt += 1
    return 1

def square_check(arr):
    cnt = 0
    for i in range(0, 9, 3):
        if cnt != 0:
            return 0
        elif cnt == 0:
            num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(0, 9, 3):
            for x in range(i+3):
                for y in range(j+3):
                    if arr[x][y] in num:
                        num.remove(arr[x][y])
                    elif arr[x][y] not in num:
                        cnt += 1
    return 1

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 행 체크 true 이면 열 체크 true 이면 네모 체크 true 이면 1 반환
    # 행 체크 열 체크 네모 체크 하다가 false 나오면 그대로 0 출력하고 멈춤

    if row_check(arr) == 1:
        if col_check(arr) == 1:
            if square_check(arr) == 1:
                print(f'#{tc} 1')
            else:
                print(f'#{tc} 0')
        else:
            print(f'#{tc} 0')
    else:
        print(f'#{tc} 0')


