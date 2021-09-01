T = int(input())
for tc in range(1, T+1):
    a, b, c = map(int, input().split())
    bread = 0
    while c > 0:
        if a < b:
            c -= a
            if c >= 0:
                bread += 1
            elif c < 0:
                break
        elif a > b:
            c -= b
            if c >= 0:
                bread += 1
            elif c < 0:
                break
    print(f'#{tc} {bread}')