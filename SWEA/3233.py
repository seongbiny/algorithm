T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())

    num = a // b
    sum = 0

    for i in range(1, num+1): # 1 2
        a = 1 + 2*(i-1)
        sum += a

    print(f'#{tc} {sum}')