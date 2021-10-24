def rotate(arr, N):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-1-j][i]
    return new_arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    '''
    [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]
    '''

    arr_90 = rotate(arr, N)
    arr_180 = rotate(arr_90, N)
    arr_270 = rotate(arr_180, N)

    print(f'#{tc} ')
    for i in range(N):
        print("".join(map(str, arr_90[i])), end=" ")
        print("".join(map(str, arr_180[i])), end=" ")
        print("".join(map(str, arr_270[i])), end=" ")
        # print()

