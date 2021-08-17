T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 00~33 을 한칸씩 전부 다 이동해야함
    result_sum = [] #m*m 네모칸만큼 다 더한 합 넣어주는 리스트
    for i in range(n-m+1): # 0 1 2 3 # 5*5 이면 0.0 ~ 3.3 까지 이동해야하므로, 6*6 이면 0.0~3.3
        for j in range(n-m+1): # 0 1 2 3  #00 01 02 03 10 11 12 13 ... 33
            sum = 0
            # m*m 행렬만큼 더해서 넣어줌
            for x in range(m): # 0 1
                for y in range(m): # 0 1 # 00 01 10 11
                    sum += arr[i+x][j+y] # 옆으로 한칸씩 이동
            result_sum.append(sum)
    #print(result_sum)
    maxV = 0
    for i in result_sum:
        if maxV < i:
            maxV = i

    print(f'#{tc} {maxV}')

    '''
        dx = [0, 0, 1, 1, 0, 1, 2, 2, 2]
        dy = [0, 1, 1, 0, 2, 2, 2, 1, 0]

        maxV = 0
        for i in range(n-1): # 0 1 2 3
            for j in range(n-1): # 0 1 2 3
                sum = 0
                for k in range(m*m):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    sum += arr[nx][ny]
                if maxV < sum:
                    maxV = sum

        print(f'#{tc} {maxV}')
    '''






