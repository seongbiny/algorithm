
def paint(r1, c1, r2, c2, color):
    #행우선
    for row in range(r1, r2):
        for col in range(c1, c2):
            (row, col)의 좌표가 비어있으면: color 색칠
            비어있지 않으면: 보라색으로 색칠

            # 방법 2: 좌표에 색이 칠해져 있는지 확인 없이 누적을 활용해 보자




T = int(input())
for tc in range(1, T+1):
    n = int(input())
    brd = 빈 보드판 만들기
    for cnt in range(n):
        r1, c1, r2, c2, color = map(int,input().split())

        print(r1, c1, r2, c2, color)

    보라색이 몇개인지 갯수를 세서 출력


