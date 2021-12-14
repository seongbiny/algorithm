from itertools import combinations
import sys
input = sys.stdin.readline

lst = [int(input()) for i in range(9)]

a = list(combinations(lst, 7))
result = []
for i in range(len(a)):
    if sum(a[i]) == 100:
        result = sorted(a[i])

for i in range(7):
    print(result[i])

