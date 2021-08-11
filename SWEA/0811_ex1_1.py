import sys
sys.stdin = open("in1.txt","r")

T = 3
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    sum = 0

    for i in range(N):
        for j in range(N):
            sum1 = 0
            for k in range(4):
                newi = i + dx[k]
                newj = j + dy[k]
                if 0 <= newi < N and 0 <= newj < N:
                    sum1 += abs(arr[newi][newj] - arr[i][j])
            sum += sum1
    print(sum)