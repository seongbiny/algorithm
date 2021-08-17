T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    n = len(str1)
    m = len(str2)

    cnt = [0] * n

    for i in range(n):
        for j in range(m):
            if str1[i] == str2[j]:
                cnt[i] += 1

    maxV = 0
    for i in range(len(cnt)):
        if maxV < cnt[i]:
            maxV = cnt[i]

    print(f'#{tc} {maxV}')