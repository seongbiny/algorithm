def mergeSort(s, e):
    global cnt
    if s+1 == e:
        return
    # 분할
    mid = (s + e) // 2
    mergeSort(s, mid)
    mergeSort(mid, e)
    # 카운팅
    if num[mid-1] > num[e-1]:
        cnt += 1
    # 병합
    i, j, k = s, mid, s
    while i < mid and j < e:
        if num[i] < num[j]:
            tmp[k] = num[i]
            i, k = i+1, k+1
        else:
            tmp[k] = num[j]
            j, k = j+1, k+1
    while i < mid:
        tmp[k] = num[i]
        i, k = i + 1, k + 1
    while j < e:
        tmp[k] = num[j]
        j, k = j + 1, k + 1
    for i in range(s, e):
        num[i] = tmp[i]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int, input().split()))
    tmp = [0] * N
    cnt = 0
    mergeSort(0, N)
    print(f'#{tc} {num[N//2]} {cnt}')