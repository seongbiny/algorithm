T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))

    sumV = []

    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                sumV.append(lst[i]+lst[j]+lst[k])

    sumV = list(set(sumV))

    sumV = sorted(sumV, reverse=True)
    # print(sumV)
    print(f'#{tc} {sumV[4]}')
