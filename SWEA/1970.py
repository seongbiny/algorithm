T = int(input())
for tc in range(1, T+1):
    won = int(input())
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    check = ['0'] * 8
    result = 0
    print(f'#{tc}')
    for i in range(len(change)):
        if won//change[i] > 0:
            check[i] = str(won//change[i])
            won -= change[i]*(won//change[i])

    result = ' '.join(check)
    print(result)




