T = int(input())
for tc in range(1, T+1):
    num, cnt = input().split()
    cnt = int(cnt)
    nums = []
    for i in range(len(num)):
        nums.append(int(num[i]))
    min_nums = nums[:]
    max_nums = nums[:]
    minmin = nums[:]
    maxmax = nums[:]
    min_index = []
    max_index = []
    min_nums.sort()
    max_nums.sort(reverse=True)

    for i in min_nums:
        min_index.append(minmin.index(i))
        minmin[minmin.index(i)] = 0

    for i in max_nums: # 7 7 3 2
        for j in range(len(maxmax)-1, -1, -1): # 3 2 1 0
            if maxmax[j] == i:
                max_index.append(j)
                maxmax[j] = 0

    while cnt > 0:


        cnt -= 1

    for i in range(len(nums)):
        nums[i] = str(nums[i])
    result = ''.join(nums)
    print(f'#{tc} {result}')


