T = int(input()) # 테스트 케이스 번호

for i in range(1,T+1):
    n = int(input()) # 주어지는 양수의 개수 n
    nums = list(map(int,input().split())) # 주어지는 양수들을 리스트에 담음

    maxV = 0 # 최대값 초기값
    minV = 10000000 # 최소값 초기값
    for z in nums:
        if maxV < z:
            maxV = z # 최대값을 내장함수 없이 구하는 과정
    for j in nums:
        if minV > j:
            minV = j # 최소값을 내장함수 없이 구하는 과정
    print(f'#{i} {maxV - minV}') # 최대값 - 최소값


