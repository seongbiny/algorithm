T = int(input())
for tc in range(1, T+1):
    a, b = map(str, input().split())
    a = list(a)
    b = list(b)

    arr = [[0]*(len(a)+2) for _ in range(len(b)+2)]

    for i in range(2, len(a)+2):
        arr[0][i] = a[i-2]
    for i in range(2, len(b)+2):
        arr[i][0] = b[i-2]

    maxv = 0
    for i in range(2, len(b)+2):
        for j in range(2, len(a)+2):
            if arr[0][j] == arr[i][0]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
                if arr[i][j] > maxv:
                    maxv = arr[i][j]

    print(f'#{tc} {maxv}')

    '''
    연속된 값 구하는게 아님 ! 비교하는 과정에서 이전의 최대 공통부분수열은 계속 유지됨됨
   [[0, 0, 'a', 'c', 'a', 'y', 'k', 'p'], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    ['c', 0, 0, 1, 1, 1, 1, 1], 
    ['a', 0, 1, 1, 2, 2, 2, 2], 
    ['p', 0, 1, 1, 2, 2, 2, 3], 
    ['c', 0, 1, 2, 2, 2, 2, 3], 
    ['a', 0, 1, 2, 3, 3, 3, 3], 
    ['k', 0, 1, 2, 3, 3, 4, 4]]
    '''
