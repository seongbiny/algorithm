n = int(input())

num = int(input())
sum = 0

for i in range(n):
    sum += num%10
    num = num//10
    
print(sum)
