import sys
input = sys.stdin.readline

N = int(input())
original = [int(input()) for _ in range(N)]
new = sorted(original)
# print(original, new)
stack = []
result = []
j = 0
for i in new:
    stack.append(i)
    result.append('+')
    if stack and stack[-1] == original[j]:
        stack.pop()
        result.append('-')
        j += 1
        