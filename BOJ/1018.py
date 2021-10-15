N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
minV = 999999
for i in range(N-8): # 0 1
    cnt = 0
    col = 0
    for j in range(M-8): # 0 1 2 3
        for col in range(8):
            if chess[i+col][j] == 'W':
                for k in range(j, j+8, 2): # 0 2 4 6
                    if chess[i+col][k] != 'W':
                        cnt += 1
                for k in range(j+1, j+8, 2): # 1 3 5 7
                    if chess[i+col][k] != 'B':
                        cnt += 1
            elif chess[i+col][j] == 'B':
                for k in range(j, j+8, 2):
                    if chess[i+col][k] != 'B':
                        cnt += 1
                for k in range(j+1, j+8, 2):
                    if chess[i+col][k] != 'W':
                        cnt += 1
        if cnt < minV:
            minV = cnt
print(minV)