T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(str, input().split()))
    ans = [''] * n

    if n%2 == 0:
        mid = n//2
    else:
        mid = n//2 + 1

    i = 0
    j = mid
    k = 0
    while k < n:
        if k % 2 == 0:
            ans[k] = arr[i]
            i += 1
        else:
            ans[k] = arr[j]
            j += 1
        k += 1

    print(''.join(ans))