T = int(input())
for tc in range(1, T+1):
    nums, cnt = input().split()
    cnt = int(cnt)
    N = len(nums)
    cur_nums = set([nums])
    next_nums = set()
    for _ in range(cnt):
        while cur_nums:
            s = cur_nums.pop()
            s = list(s)
            for i in range(N):
                for j in range(i+1, N):
                    s[i],s[j] = s[j],s[i]
                    next_nums.add(''.join(s))
                    s[i],s[j] = s[j], s[i]
        cur_nums, next_nums = next_nums, cur_nums

    print(f'#{tc} {max(map(int,cur_nums))}')
