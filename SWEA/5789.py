T = int(input())
for tc in range(1, T+1):
    n, q = map(int, input().split())
    lst = [0] * n
    for i in range(q):
        l, r = map(int, input().split())

        for j in range(l, r+1): # 1 2 3
            lst[j-1] = i+1

    lst = list(map(str, lst))
    result = ' '.join(lst)
    print(f'#{tc} {result}')