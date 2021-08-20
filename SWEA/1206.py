T =10
for tc in range(1, T+1):
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(2, len(h)-2):
        lst = [h[i-2], h[i-1], h[i+1], h[i+2]]
        maxV = 0
        for j in range(len(lst)):
            if maxV < lst[j]:
                maxV = lst[j]
        if h[i] - maxV > 0:
            cnt += h[i] - maxV
    print(f'#{tc} {cnt}')







