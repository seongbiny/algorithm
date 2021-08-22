T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))

    sum = 0
    for i in range(len(nums)):
        sum += nums[i]

    result = sum / len(nums)

    print(f'#{tc} {result:.0f}')

