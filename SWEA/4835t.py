
for tx in range(1, TC+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))

    #maxV = 0 # 나올 수 있는 합 중 제일 작은 값
    #minV = 10000 * 100 * 1 # 나올 수 있는 합 중 가장 큰 값
    sumV = 0 # 0번째 합을 한번 구해 놓는다.
    for i in range(M):
        sumV += Ai[i]
    maxV = sumV
    minV = sumV
    for i in range(1, N-M+1):
        #i 번재 합은
        ithS = ithS - 첫번째 + 마지막번째

        if maxV < ithS:
            maxV = ithS

        if minV > ithS:
            minV = ithS

    print()