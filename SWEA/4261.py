T = int(input())

phone = [
    [0],
    [0],
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z']
]

for tc in range(1, T+1):
    S, N = map(int, input().split()) # ['6', '6', '6', '6', ' ', '3']
    words = list(map(str, input().split())) # ['tomo', 'mono', 'dak']

    nums = list(str(S))
    #print(nums)
    result = 0

    for j in range(N):
        cnt = 0
        if len(words[j]) == len(nums):
            for i in range(len(nums)): # 0 1 2 3
                if words[j][i] in phone[int(nums[i])]:
                    cnt += 1
                else:
                    break

        if cnt == len(nums):
            result += 1

    print(f'#{tc} {result}')




