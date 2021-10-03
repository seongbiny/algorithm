T = int(input())
for tc in range(1, T+1):
    num, cnt = input().split()
    cnt = int(cnt)
    nums = []
    for i in range(len(num)):
        nums.append(num[i])
    new_nums = sorted(nums)

    min_index = []
    max_index = []
    for i in range(len(nums)):
        a = nums.index(new_nums[i])
        min_index.append(a)
        nums[a] = 99999
    for i in range(len(nums)):
        pass

    print(min_index, max_index)

    # for i in range(cnt):
    #     if len(nums) == 2:
    #         nums[0], nums[1] = nums[1], nums[0]
    #     else: #최소값과 인덱스가 큰 최대값 자리를 바꾼다.
    #         nums[min_index[i]], nums[max_index[i]] = nums[max_index[i]], nums[min_index[i]]



