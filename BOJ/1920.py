import sys

N = int(sys.stdin.readline())
anums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
bnums = list(map(int, sys.stdin.readline().split()))
anums.sort()

for i in range(M):
    result = 0
    left = 0
    right = N-1
    if bnums[i] <= anums[-1]:
        while left <= right:
            mid = (left + right) // 2
            if bnums[i] == anums[mid]:
                result = 1
                break
            elif bnums[i] > anums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        print(result)
    else:
        print(result)
