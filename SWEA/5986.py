# 소수 구하기
a = [False, False] + [True] * 1000
lst = []
for i in range(2, 1000):
    if a[i]:
        lst.append(i)
        for j in range(2*i, 1000, i):
            a[j] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for i in range(len(lst)):
        if N < lst[i]:
            break
        for j in range(i, len(lst)):
            if N < lst[i] + lst[j]:
                break
            for k in range(j, len(lst)):
                if N < lst[i] + lst[j] + lst[k]:
                    break
                if N == lst[i] + lst[j] + lst[k]:
                    if lst[i] <= lst[j] <= lst[k]:
                        cnt += 1

    print(f'#{tc} {cnt}')
