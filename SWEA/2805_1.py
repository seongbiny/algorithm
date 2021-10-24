T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]
    sumV = 0
    c = N//2
    col = [c, c-1, c+1, c-2, c+2, c-3, c+3]
    for i in range(c): # 0 1
        for j in range(0, i*2+1): # 0, 0,1,2 ,0,1,2,3,4
            sumV += arr[col[j]][i]
            #print(arr[col[j]][i], end=' ')
    i = 0
    for i in range(N-1, c-1, -1): # 4 3 2
        for j in range(0, i*2+1): # 0 012 01234
            sumV += arr[col[j]][i]
            # print(arr[col[j]][i], end=' ')
            i += 1

    print(sumV)