T = int(input())
for tc in range(1, T+1):
    N, W = map(int, input().split())
    nums = list(map(int, input().split()))

    lst = []

    for i in range(1<<len(nums)):
        sub_lst=[]
        for j in range(len(nums)):
            if i & (1<<j):
                sub_lst.append(nums[j])
        lst.append(sub_lst)
    cnt = 0
    for i in range(len(lst)):
        if sum(lst[i]) == 10:
            cnt += 1
    print(cnt)