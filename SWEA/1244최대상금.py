def swap(a):
    global cnt
    cur_nums = int("".join(nums))
    if a == change:
        cnt = max(cnt, cur_nums)
        return

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            swap(a+1)
            nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for tc in range(1, T+1):
    nums, change = input().split()
    nums = list(nums)

    change = int(change)
    cnt = 0

    swap(0)
    print(f'#{tc} {cnt}')