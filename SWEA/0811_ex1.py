import sys
sys.stdin = open("in1.txt","r")

T = int(input())

dcol = [0, 0, -1, 1]
drow = [-1, 1, 0, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        nums = list(map(int, input().split()))
        for j in range(N):
            arr[i][j] = nums[j]

    result = 0
    for row in range(N):
        for col in range(N):
            sum = 0
            for mode in range(4):
                newrow = row + drow[mode]
                newcol = col + dcol[mode]
                if 0 <= newrow < N and 0 <= newcol < N:
                    #print(arr[row][col], arr[newrow][newcol])
                    sum += abs(arr[row][col] - arr[newrow][newcol])
            result += sum

    print(f'#{tc} {result}')