T = int(input())
for tc in range(1, T+1):
    m, d = map(int, input().split())

    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #day = [4, 0, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3]

    day = 0
    for i in range(m-1):
        day += mon[i]

    day += d
    day = day % 7
    result = (day + 3) % 7
    print(f'#{tc} {result}')



