import sys
sys.stdin = open("input_1974.txt","r")


    # 열 확인
    # 네모 확인

T = int(input())
for tc in range(1, T+1):
    cnt = 0
    n = 9
    arr = [list(map(int,input().split())) for _ in range(n)]
    a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    #b = [[0]*9 for _ in range(9)]
    c = []
    # 행 확인
    for r in range(9):
        if len(set(arr[r])) == 9:

    for c in range(9):
        c.append(arr[j][i])
        if len(set(c)) == 9:
            cnt += 1
                                            죄 송 해 요 모 르 겠 어 요 . . .
    print(f'#{tc} {cnt}')