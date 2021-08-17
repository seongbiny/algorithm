def check(str1, str2):
    n = len(str1)
    m = len(str2)

    for i in range(n-m+1):
        j = 0
        while j < n and str1[j] == str2[i+j]:
            j += 1

        if j == n:
            return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    p = input()
    t = input()

    print(f'#{tc} {check(p, t)}')