T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())

    maxv, minv = 0, 0

    if a+b > n:
        maxv = min(a, b)
        minv = a+b-n
    elif a+b <= n:
        maxv = min(a,b)
        minv = 0
    if a == b == n:
        maxv = n
        minv = n

    print(f'#{tc} {maxv} {minv}')

