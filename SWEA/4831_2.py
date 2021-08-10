t = int(input())

for num in range(1,t+1):
    K,N,M = map(int, input().split())

    charge = list(map(int, input().split()))

    #N까지 도착하기위한 중간점
    cnt = 0
    #충전소를 거친 횟수
    count = 0
    # 도착점인 N을 넘어갈때까지 반복문
    while cnt < N:
        if cnt + K >= N:   # 만약 중간지점 + 한번 충전한양 -> 브레이크
            break;
        else:             #아니면 반복문을 통해 가장 효율적인 충전소 찾아서 cnt,count 증가
            for i in range(K):
                if (cnt + K - i) in charge:
                    cnt += (K-i)
                    count += 1
                    break
            else:             # 아무것도 해당하지 않으면 count에 0을 저장하고 브레이크
                count = 0
                break

    print(f'#{num} {count}')