T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))

    sum = 0
    for i in range(10):
        if nums[i] % 2 == 1:
            sum += nums[i]

    print(f'#{tc} {sum}')
