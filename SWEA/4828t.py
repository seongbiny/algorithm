
def myMax():
    maxV = Ai[0]
    for i in range(1, N):
        if maxV < Ai[i]:
            maxV = Ai[i]
    return maxV
def myMin():
    minV = Ai[0]
    for j in range(1, N):
        if minV > Ai[j]:
            minV = Ai[j]
    return minV

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Ai = list(map(int, input().split()))

    maxV = myMax(Ai) # 최대값을 구하는 과정을 함수로 따로 빼놈
    minV = myMin(Ai) # 최소값을 구하는 과정을 함수로 따로 빼놈
    result = maxV - minV

    print(f'#{tc} {result}')

    # 런타임에러 ;;