T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for i in B:
        s = 0
        e = N-1

        flag = 0
        while s <= e:
            mid = (s + e) // 2

            if i == A[mid]:
                cnt += 1
                break
            elif i < A[mid]:
                e = mid - 1
                if flag == 1:
                    break
                flag = 1
            else:
                s = mid + 1
                if flag == -1:
                    break
                flag = -1
    print(f'#{tc} {cnt}')
