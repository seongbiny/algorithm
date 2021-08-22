n = int(input())
nums = list(map(int, input().split()))

# 중간값 인덱스 = (len(nums)-1)//2

for i in range(n-1, 0, -1):
    for j in range(0, i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums[(len(nums)-1)//2])

