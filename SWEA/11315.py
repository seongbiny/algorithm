# 8방향 체크

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    cnt = 0
    result = 0
    # 행방향 우선 순회
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'o': # 행방향으로 돌다가 o 를 만나면 카운트 +1
                cnt = 1
                for k in range(8): # 그 자리에서 8방향으로 돈다.
                    newi = i + dx[k]
                    newj = j + dy[k]
                    while 0 <= newi < n and 0 <= newj < n and arr[newi][newj] == 'o': # 새로 간 방향에 0 이 있을때까지 쭉 간다
                        arr[i][j] = arr[newi][newj] # 현재 위치를 옮긴 위치로 변경
                        cnt += 1 # 그 자리에 o가 있어서 옮긴거니까 카운트 +1
                        newi = newi + dx[k] # 같은 방향으로 쭉 나간다
                        newj = newj + dy[k]
                        if cnt >= 5: # 돌다가 o를 5개 세면
                            result = 1 # 결과값에 1 넣고
                            break # 와일문 탈출
                        if (0 > newi or newi >= n) or (0 > newj or newj >= n) or arr[newi][newj] == '.': # 새로운 방향으로 쭉 나가다가 범위에 벗어나면 카운트 초기화
                            cnt = 1


    #print(f'#{tc} {result}')

    if result == 1:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')


