T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))

    maxV = 0
    for i in range(n):
        for j in range(i+1, n):
            int_target = lst[i] * lst[j]
            target = str(int_target)
            if len(target) > 1:
                for k in range(len(target)-1):
                    if target[k] > target[k+1]:
                        break
                    else:
                        if int_target > maxV:
                            maxV = int_target

    if maxV == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {maxV}')










