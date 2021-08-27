T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    guest = list(map(int, input().split()))

    time = [0] * (max(guest)+1)
    bread = 0

    for i in range(len(time)):
        if i != 0 and i % m == 0:
            bread += k
        if i in guest:
            bread -= 1
            if bread < 0:
                print(f'#{tc} Impossible')
                break
    if bread >= 0:
        print(f'#{tc} Possible')









