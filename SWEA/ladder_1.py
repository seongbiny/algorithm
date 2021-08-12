import sys
sys.stdin = open('input_ladder.txt')

t = 10
N = 100

for num in range(1, t + 1):
    z = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):  # 마지막행 열번호를 찾아서 뒤에서부터 탐색시작
        if arr[99][i] == 2:
            goal = i

    x = 99
    y = goal

    while x != 0:
        x -= 1
        if y == 0:  # 맨왼쪽은 왼쪽으로 못가니 오른쪽 1아니면 위로이동
            if arr[x][y + 1] == 1:
                y += 1
                while arr[x][y + 1] != 0:
                    y += 1
            else:
                pass
        elif y == 99:  # 맨오른쪽은 오른쪽으로 못가니 왼쪽 아니면 위로 이동
            if arr[x][y - 1] == 1:
                y -= 1
                while arr[x][y - 1] != 0:
                    y -= 1
            else:
                pass
        else:  # 1열~98열까지  왼,오른쪽 인덱스가 1이면 이동 아니면 위로
            if arr[x][y + 1] == 1:
                y += 1
                while arr[x + 1][y] != 1:
                    y += 1

            elif arr[x][y - 1] == 1:
                y -= 1
                while arr[x - 1][y] != 1:
                    y -= 1
            else:
                pass

    print(f'#{num} {y}')