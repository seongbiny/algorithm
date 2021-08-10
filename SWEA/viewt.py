import sys
sys.stdin = open("input.txt","r")

def getMax(a, b, c, d):
    maxV = a
    if maxV < b:
        maxV = b
    if maxV < c:  #elif 쓰면? 안돼
        maxV = c
    if maxV < d:
        maxV = d

    return maxV


def getMax(curI):
    maxV = BUILD[curI-2]
    for i in range(curI-2, curI+3):
        if i == curI:
            continue
        if maxV < BUILD[i]:
            maxV = BUILD[i]
    return maxV

TC = 10
for tc in range(1, TC+1):
    N = int(input())
    BUILD = list(map(int, input().split()))

    result = 0
    for i in range(2, N-2):
        #1h = getMax(BUILD[i-2], BUILD[i-1], BUILD[i+1], BUILD[i+2])
        h = getMax(i)
        if BUILD[i] > h:
            # ith = BUILD[i] - h
            result += BUILD[i] - h
    print('#{} {}'.format(tc, result))
