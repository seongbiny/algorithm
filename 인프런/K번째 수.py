t = int(input())
for _ in range(t):
    n, s, e, k = map(int, input().split())
    lst = list(map(int, input().split()))

    # print(lst[s:e+1].sort())
    result = lst[s-1:e]
    result.sort()
    # print(result)
    print(result[k-1])