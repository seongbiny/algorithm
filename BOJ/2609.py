import sys
input = sys.stdin.readline

a, b = map(int, input().split())

c = min(a, b)
gcf = 0
for i in range(c, 0, -1):
    if a % i == 0 and b % i == 0:
        gcf = i
        break

lcm = (a // gcf)*b
print(gcf)
print(lcm)