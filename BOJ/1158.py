import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(i for i in range(1, n+1))

result = []
idx = k-1
while True:
    result.append(str(lst.pop(idx)))
    if not lst:
        break
    idx += k-1
    if idx >= len(lst):
        idx = idx % len(lst)

print(f'<{", ".join(result)}>')



