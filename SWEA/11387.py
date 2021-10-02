T = int(input())
for tc in range(1, T+1):
    d, l, n = map(int, input().split())

# 기본 데미지 = d
# 다음 데미지
    next_d = d*(1+n*l/100)

    result = 0

    for i in range(n):
        result += (d*(1+i*l/100))

    print(f'#{tc} {int(result)}')