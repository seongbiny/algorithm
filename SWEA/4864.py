
T = int(input())
for tc in range(1, T+1):
    p = input()
    t = input()
    n = len(p)
    m = len(t)

    result = 0

    for i in range(m-n+1):
        if t[i:i+n] == p:
            result = 1

    print(f'#{tc} {result}')




