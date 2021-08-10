T = int(input()) #테스트케이스 번호
for i in range(1, T+1):
    n = int(input()) # 카드 장수
    card = list(map(int, input())) # 주어지는 카드를 리스트에 담음

    counts = [0] * 10 # 카운팅 정렬을 위해 빈 리스트를 만들어준다

    for j in range(n): # card 리스트를 돌면서 카운팅정렬 해준다.
        p = card[j]
        counts[p] += 1

    maxV = counts[0] # 최대값 초기화
    pos = 0 # 카드의 위치 초기화
    for k in range(len(counts)): # 카운트리스트에서 가장 많은 수를 찾는 과정
        if maxV <= counts[k]:
            maxV = counts[k]
            pos = k # 그 최대값의 인덱스위치

    print(f'#{i} {pos} {maxV}')