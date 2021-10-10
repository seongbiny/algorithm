def move(idx, e, c):
    global ans
    if idx == bus_stop[0]:
        if ans > c:
            ans = c
    else:
        # 배터리를 교체하지 않고 내려보내기
        if e > 0:
            move(idx+1, e-1, c)
        # 배터리를 교체하고 내려보내기
        if c < ans:
            move(idx+1, bus_stop[idx]-1, c+1)

T = int(input())
for tc in range(1, T+1):
    bus_stop = list(map(int, input().split()))
    ans = 9999999
    move(2, bus_stop[1]-1, 0)
    print(f'#{tc} {ans}')