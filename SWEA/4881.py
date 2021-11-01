# 순열 문제 이다 !!!!!!!!!!!!

def per(row):
    global minV, sumV
    if sumV > minV:
        return
    if row==n:
       if sumV < minV:
           minV = sumV
           return

    for col in range(n):
        if not visited[col]:
            # 확장
            visited[col] = True
            sumV += arr[row][col]
            per(row + 1)
            # 축소
            sumV -= arr[row][col]
            visited[col] = False


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [False] * n
    sumV = 0
    minV = 10 * n
    per(0)
    print(f'#{tc} {minV}')





