def gcd_get(a, b):
    if a > b:
        for j in range(b, 0, -1):
            if a % j == 0 and b % j == 0:
                return int(j)

n = int(input())
lst = list(map(int, input().split()))

gcd = lcm = lst[0]
for i in range(1, n+1):
    gcd = gcd_get(gcd, lst[i])
    # lcm = lcm // gcd_get(lcm, lst[i]) * lst[i]

print(gcd_get(lcm, lst[1]))
