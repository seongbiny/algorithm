import sys
sys.stdin = open("input_sum.txt","r")

T = 10
for tc in range(1, T + 1):  # 테스트케이스 10개 반복

    num = int(input())  # 테스트 케이스 번호 입력
    nums = [list(map(int, input().split())) for _ in range(100)]  # 100X100 2차배열 입력

    result = []

    # len(nums) 는 열의 개수

    for i in range(100):
        sumV = 0
        for j in range(100):
            sumV += nums[i][j]
        result.append(sumV)

    for i in range(100):
        sumV = 0
        for j in range(100):
            sumV += nums[j][i]
        result.append(sumV)

    sumV = 0
    for i in range(100):
        sumV += nums[i][i]
    result.append(sumV)

    sumV = 0
    for i in range(100):
        sumV += nums[i][100 - i - 1]
    result.append(sumV)

    maxV = 0
    for z in range(len(result)):
        if maxV < result[z]:
            maxV = result[z]

    print(f'#{tc} {maxV}')
