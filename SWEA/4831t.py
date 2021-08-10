#1 정류장을 기준으로
#2 충전기를 기준으로

TC = int(input())
for tc in range(1, TC+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    curp = 0
    cnt = 0

    while curp < N:
        nextp = curp + K
        if nextp >= N:
            break
        if nextp in charge: # 충전기가 있나? 갈수 있나?
            cnt += 1
            curp = nextp
        else: # 충전기가 없으면
            #nextp 의 값을 하나씩 빼면서(앞으로 가면서) 충전기가 있는지 확인
            #nextp 에서 curp 전까지 충전기가 있는지 확인 한다.
            while curp < nextp and nextp not in charge:
                nextp -= 1
            if curp == nextp: #충전기가 없다는 뜻
                cnt = 0
                break
            else: #nextp in charge: #충전기가 하나 있다
                cnt += 1
                curp = nextp

    print(f'#{tc} {cnt}')





    # 마지막 충전했던 위치 = 0
    #[4, 7, 9, 14, 17]
    #k=5
    charge.insert(0, 0)
    charge.append(N)
    lastp = 0
    cnt = 0
    for i in range(1, len(charge)):
        # 충전기 사이의 거리를 확인한다.
        if charge[i] - charge[i-1] > K:
            cnt = 0
            break
        #i 번째에 있는 충전기에서 충전여부를 결정한다.
        #i번째에서 충전 여부 결정할 수 없음.
        if charge[i] > lastp + K:
            lastp = charge[i-1]
            cnt += 1

    print(f'#{i} {tc} {cnt}')



    
