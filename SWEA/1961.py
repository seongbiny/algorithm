T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 2차배열 받음

    #def turn_90():
    newarr = []
    dx = [2, 1, 0, 1, 1, 0, -1, 2]
    dy = [0, -1, -2, 1, -1, 2, 1, 0]
    '''
    0: arr[i+dx[0]][i+dy[0]]
    1: arr[i+dx[1]][i+dy[1]]
    2: arr[i+dx[2]][i+dy[2]]
    ...
    '''
    for i in range(N): # 0 1 2
        for j in range(N): # 0 1 2
         # 0 1 2 3 4 5 6 7
            newi = i +dx[j] # 0+0
            newj = j +dy[j] # 0+0
            if 0 <= newi < N and 0 <= newj < N:
                print(arr[newi][newj])

    #print(newarr)
