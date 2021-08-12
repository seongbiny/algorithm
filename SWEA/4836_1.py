import sys
sys.stdin = open("input_4836.txt","r")

def paint(r1, c1, r2, c2, color):
    for row in range(r1, r2+1): # 주어진 열 처음부터 끝까지
        for col in range(c1, c2+1): # 주어진 행 처음부터 끝까지
            if arr[row][col] == 0: # color 색칠
                arr[row][col] = color # 주어진 색으로 칠한다
            else: # 칸에 어떤 색이 이미 칠해져 있다면
                arr[row][col] = 3  # 보라색으로 칠한다

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list([0] * 10) for _ in range(10)]
    for cnt in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        paint(r1, c1, r2, c2, color)
        result = 0 # 보라색 몇개인지 담을 거
    for i in range(len(arr)): # 행 우선탐색 돌린다
        for j in range(len(arr[i])):
            if arr[i][j] == 3:
                result += 1

    print(f'#{tc} {result}')

