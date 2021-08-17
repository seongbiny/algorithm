T = int(input())
for tc in range(1, T+1):
    str1, str2 = input().split()

    n = len(str1)
    m = len(str2)
    cnt = 0
    idxT = 0
    while idxT < n-m+1:
    #for idxT in range(n-m+1): #마지막위치 계산하는거 외우자
        idxP = 0
        while idxP < m and str1[idxT+idxP] == str2[idxP]:
            idxP += 1
        if idxP == m:
            cnt += 1
            idxT += idxP # m 도 가능
        else: #패턴 못찾았을때
            idxT += 1

    print(f'#{tc} {cnt}')