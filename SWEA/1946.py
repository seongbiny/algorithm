T = int(input())
for tc in range(1, T+1):
    n = int(input())
    result = ''
    for i in range(n):
        a, b = input().split()
        b = int(b)
        result += a*b
    print(f'#{tc}')

    for i in range(len(result)):
        if (i+1)%10 == 0:
            print(result[i])
        else:
            print(result[i], end="")
    print()

