#가로축순회 하고 회문 못찾으면 세로축순회
#가로축 처음인덱스와 끝인덱스 비교비교비교

T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    arr = [input() for _ in range(n)]
    result = 0
    newnewarr=[]
    # 가로축에서 회문 찾기
    for i in range(n): # 0 1 2 3 4 5 6 7 8 9
        for j in range(n-m+1): # 0 1 2 3 4
            if arr[i][j:j+m] == arr[i][j:j+m][::-1]:
                result = ''.join(arr[i][j:j+m])

    # 세로축에서 회문 찾기
    # 세로축은 슬라이싱 안되니까 행 열 자리 바꿔주자
    for i in range(n):
        newarr = []
        for j in range(n):
            newarr += arr[j][i]
        newnewarr.append(''.join(newarr))

    for i in range(n): # 0 1 2 3 4 5 6 7 8 9
        for j in range(n-m+1): # 0 1 2 3 4
            if newnewarr[i][j:j+m] == newnewarr[i][j:j+m][::-1]:
                result = ''.join(newnewarr[i][j:j+m])

    print(f'#{tc} {result}')



