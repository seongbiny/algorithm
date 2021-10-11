T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = ''
    for i in range(100,-1,-1):
        result += str(M//(2**i))
        M %= (2**i)
    if result[-1:-N-1:-1] == '1'*N:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')
