T = int(input())
for tc in range(1, T+1):
    n = input()
    nums = list(map(int, input().split()))
    lst = []
    for i in nums:
        if i not in lst:
            lst.append(i)

    result = []
    for i in lst:
        result.append(nums.count(i))

    max = 0
    idx = 0
    for i in range(len(result)):
        if max < result[i]:
            max = result[i]
            idx = i

    print(f'#{tc} {lst[idx]}')