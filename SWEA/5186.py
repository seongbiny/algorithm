T = int(input())

for tc in range(1, T+1):
    N = float(input())
    result = ''
    for i in range(-1, -14, -1):
        result += str(int(N // (2**i)))
        N %= (2**i)
        if N == 0:
            break
    else:
        result = 'overflow'

    print(f'#{tc} {result}')

