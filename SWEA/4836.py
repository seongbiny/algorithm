T = int(input())
for tc in range(1, T+1):
    n = int(input())
    color = [list(map(int, input().split())) for _ in range(n)]
    # 1 먼저 칠하고 2 칠할때 1이 있는 곳을 체크
    arr = [[0] * 10 for _ in range(10)] # 10*10 배열
    cnt = 0 #
    # r1 2.2 4.4

    for z in range(n):
        for i in range(color[z][0], color[z][2]+1): # 2, 3, 4
            for j in range(color[z][1], color[z][3]+1): # 2 3 4
                # arr[i][j] 에 색이 있을때
                #if arr[i][j] == 1 or arr[i][j] == 2:

                # 색이 없을때
                #if arr[i][j] == 0
                if arr[i][j] == 0:
                    if color[z][-1] == 1:
                        if arr[i][j] == 1:
                            pass
                        arr[i][j] = 1
                    if color[z][-1] == 2:
                        if arr[i][j] == 1:
                            cnt += 1
                        arr[i][j] = 2
                if arr[i][j] != 0:


    print(f'#{tc} {cnt}')


