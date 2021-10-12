
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    # 부분 수열 중
    # 각 원소가 이전 원소보다 크다는 조건
    #check = [0]*N
    result = 0
    for i in range(N): # 수열 순회 # 1 2 3 4
        for j in range(i): #
            if lst[j] > lst[i]:

            if result < maxV:
                result = maxV
    print(f'#{tc} {result}')
