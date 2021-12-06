n = int(input())
nums = list(map(int, input().split()))
num = int(input())

result = 0
answer = 0
for i in range(n):
    if num % nums[i] == 0 and num >= nums[i]:
        result += nums[i]
    if nums[i] % num == 0 and num <= nums[i]:
        answer += nums[i]

print(result)
print(answer)