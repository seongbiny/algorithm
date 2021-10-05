def solve(x,y,sub_sum):
    global total
    if sub_sum > total:
        return
    if x == N-1 and y == N-1: #어디까지 돌껀지
        if total > sub_sum:
            total = sub_sum
        return

    #오른쪽
    if x+1 < N:
        solve(x+1,y,sub_sum+e[y][x+1])
    #아래
    if y+1 < N:
        solve(x,y+1,sub_sum+e[y+1][x])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    e = [list(map(int,input().split())) for _ in range(N)]

    total = N*N*13
    solve(0,0,e[0][0])
    print(f'#{tc} {total}')

