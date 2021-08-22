def myMax(nums):
    maxV = nums[0]

    for num in nums:
        if maxV < num:
            maxV = num
    return maxV

def arrSum(direction, r=0, c=0): # 지정한 방향으로 진행하며 합을 구하는 함수
    result = 0

    if direction[1] < 0:
        c = 99

    for _ in range(100):
        result += arr[r][c]
        r += direction[0]
        c += direction[1]

    return result

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    drc = [
        (1,0),
        (0,1),
        (1,1),
        (1,-1)
    ]

    sum_list = []

    for n in range(100):
        sum_list.append(arrSum(drc[0], c=n))
        sum_list.append(arrSum(drc[1], r=n))

    for rc in drc[2:]:
        sum_list.append(arrSum(rc))