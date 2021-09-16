T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(int(input()))

    cnt = 0
    avg = sum(lst)//len(lst)

    while lst[:] != [avg] * len(lst):
        maxV = max(lst)
        minV = min(lst)
        maxV -= 1
        minV += 1
        cnt += 1

    print(cnt)

    # print([avg] * len(lst))



