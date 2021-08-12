def getMaxPos(lst):
    maxP = 0
    n = len(lst)
    for j in range(1, n):
        if lst[maxP] < lst[j]:
            maxP = j
    return maxP

def getMinPos(lst):
    minP = 0
    n = len(lst)
    for j in range(1, n):
        if lst[minP] > lst[j]:
            minP = j
    return minP

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    ai = list(map(int,input().split()))

    for i in range(0, n): # 0 1 2 3 4 ... 9
        if i % 2 == 0:
            maxP = i + getMaxPos(ai[i:])
            ai[maxP], ai[i] = ai[i], ai[maxP]
        else:
            minP = i + getMinPos(ai[i:])
            ai[minP], ai[i] = ai[i], ai[minP]

    print(f'#{tc}', end=' ')
    for z in range(10):
        print(ai[z], end=' ')
    print()



