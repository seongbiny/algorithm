T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = ''
    for i in range(1, 13):
        N *= 2
        result += str(int(N)%2)
        if N % 1 == 0:
            break
    else:
        # 12번 동안 안되면
        result = 'overflow'
    print(f'#{tc} {result}')
