n = 1000000
a = [False, False] + [True] * (n - 1)
prime = []
for i in range(2, n + 1):
    if a[i]:
        prime.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

T = int(input())
for tc in range(1, T+1):
    # d = 포함하는 숫자, a 이상 b 이하 중
    D, A, B = map(int, input().split())

    cnt = 0

    for i in prime:
        if A <= i <= B:
            if str(D) in list(str(i)):
                cnt += 1
        if B < i:
            break

    print(f'#{tc} {cnt}')




