'''
num = int(input()) # 테스트 케이스 번호 입력
nums = [list(map(int,input().split())) for _ in range(3)] # 100X100 2차배열 입력

result = []
    #def N_turn(nums):

for i in range(len(nums)):
    sumV = 0
    for j in range(len(nums[i])):
        sumV += nums[i][j]
        result.append(sumV)

    #def M_turn(nums):

for i in range(len(nums[0])):
    sumV = 0
    for j in range(len(nums)):
        sumV += nums[j][i]
        result.append(sumV)

    #def x_turn(nums):

for i in range(len(nums)):
    result.append(nums[i][i])

    #def y_turn(nums):

for i in range(len(nums)):
    sumV = 0
    for j in range(-1, len(nums)-1, -1):
        sumV = nums[j][i]
        result.append(sumV)


print(max(result))
'''

for num in range(1,11):
    N = 100
    M = 100
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_max = 0

    for i in range(M):
        sum1 = 0
        for j in range(N):
            sum1 += arr[i][j]
        if sum1 > sum_max:
            sum_max = sum1

    for j in range(M):
        sum1 = 0
        for i in range(N):
            sum1 += arr[i][j]
        if sum1 > sum_max:
            sum_max = sum1

    for i in range(M):
        sum1 = 0
        sum1 += arr[i][i]

        if sum1 > sum_max:
            sum_max = sum1

    for i in range(M):
        sum1 = 0
        sum1 += arr[i][M-i-1]

        if sum1 > sum_max:
            sum_max = sum1

    print(f'#{num} {sum_max}')