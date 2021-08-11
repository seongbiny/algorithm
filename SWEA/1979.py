import sys
sys.stdin = open("input_1979.txt","r")

T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split()) #N*N 크기 단어길이 : K
    #for z in range(N):
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum = 0
        # 행우선탐색
    for i in range(N): # 0 1 2 3 4
        cnt = 0
        for j in range(N): # 0 1 2 3 4
            if arr[i][j] == 0:  # 행이 바뀌기 전에 1이 k일때 있다면 체크
                if cnt == K:
                    sum += 1
                    cnt = 0
            else: # 흰칸일때 체크
                cnt += 1
        if cnt > K:
            cnt = 0
        if cnt == K:
            sum += 1

    sum = 0
        # 열우선탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 0:
                if cnt == K:
                    sum += 1
                    cnt = 0
            else:
                cnt += 1
        if cnt > K:
            cnt = 0
        if cnt == K:
            sum += 1

    print(f'#{tc} {sum}')

