TC = 10
for tc in range(TC):
    no = int(input())
    #vrd = [[0] * 100 for _ in range(100)]
    #for i in range(100):
    #    vrd[i] = list(map(int, input().split()))
    #
    brd = [list(map(int, input().split())) for _ in range(100)]


    #행우선(가로축)으로 보면서 각 행의 합을 구해 maxV 를 구한다.


    #열우선(세로축)으로 보면서 각 열의 합을 구해 maxV를 구한다.
    #행,열 나누지말고 한번에 해결해보기? 좌표가 같잖아 100*100

    #왼쪽 대각선
    for i in range(99):
        brd[i][i]

    #오른쪽 대각선 0,99 / 1,98 / 2,97
    for i in range(99):
        brd[i][99-i]

    result = 0
    # ....

    print(f'#{no} {result}')
