T = int(input())
for i in range(1,T+1):
    N, M = map(int,input().split())
    nums = list(map(int,input().split()))
    result = []

    for j in range(N-M+1): #0~9
        result.append(sum(nums[j:M+j])) #012 123 234 345 456 567 678 789 7:10

    #print(f'#{i} {max(result)-min(result)}')

    maxV = 0
    minV = 10000000
    for z in result:
        if maxV < z:
            maxV = z
        if minV > z:
            minV = z
    print(f'#{i} {maxV-minV}')

    # N개의 정수가 들어있는 리스트에서 M개씩 슬라이싱하여 합을 구해 새로운 리스트에 담았다
    # 그 리스트에서 최대 - 최소