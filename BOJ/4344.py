t = int(input())
for tc in range(1, t+1):
    lst = list(map(int, input().split()))

    mean = (sum(lst) - lst[0])/lst[0]
    cnt = 0
    for i in range(1, len(lst)):
        if lst[i] > mean:
            cnt += 1
    print(f"{(cnt/lst[0])*100:.3f}%")