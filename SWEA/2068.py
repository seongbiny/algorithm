T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))

    maxV = 0
    for i in range(len(nums)):
        if maxV < nums[i]:
            maxV = nums[i]
    print(f'#{tc} {maxV}')