a, b = map(int, input().split())
maxV = 0
if a > b :
    for i in range(1, b+1):
        if a % i == 0 and b % i == 0:
            if i > maxV:
                maxV = i
else:
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            if i > maxV:
                maxV = i

print(maxV)
print(a*b//maxV)