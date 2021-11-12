T = int(input())
for tc in range(1, T+1):
    N = int(input())
    left = []
    right = []
    for i in range(N):
        l, r = map(int, input().split())
        left.append(l)
        right.append(r)

    result = 0
    for l in range(N):
        minV = 99999
        idx = 0
        for r in range(N):
            v = (left[l]**2) + (right[r]**2)
            if v < minV and idx != r:
                idx = r
                result += v

    print(result)


