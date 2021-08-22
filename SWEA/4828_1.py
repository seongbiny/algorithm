T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    # 1. 반복문을 이용한 방법
    # maxV = nums[0]
    # minV = nums[0]
    #
    # for i in nums:
    #     if  i > maxV:
    #         maxV = i
    #
    #     if i < minV:
    #         minV = i
    #
    # result = maxV - minV
    # print(f'#{tc} {result}')

    # 2. 정렬을 이용한 방법

    result = ''

    for i in range(n-1, 0, -1): # 리스트 마지막 구간까지 보겠다 4 3 2 1
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    result = nums[-1] - nums[0]

    print(f'#{tc} {result}')