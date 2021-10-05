from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = ''
    check = 0

    while len(nums) != N:
        nums += ''.join(input().strip().split())

    while True:
        if str(check) not in nums:
            break
        check += 1

    print(f'#{tc} {check}')