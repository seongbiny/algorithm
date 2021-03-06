#카운팅정렬

def getMaxPos(): # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력
    maxV = COUNTS[0]
    maxP = 0
    for j in range(1, len(COUNTS)):
        if maxV < COUNTS[j]:
            maxV = COUNTS[j]
            maxP = j
    if maxV == 1:
        maxP = max(CARDS)
    return maxP

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    CARDS = list(map(int, input())) #붙어있는 문자열을 따로따로 떨어뜨림

    COUNTS = [0] * 10 # 카운팅정렬을 위해 빈 리스트 생성

    for i in range(N):
        p = CARDS[i]
        COUNTS[p] += 1 #카운팅정렬

    # COUNTS 배열에서 최댓값을 구한다.
    # 최댓값이 있는 배열의 위치와 값을 구한다.
    maxpos = getMaxPos() #최대값이 들어있는 위치를 구해서 return 한다.

    if all(COUNTS) == 1:
        COUNTS[maxpos] = max(CARDS)

    print(f'#{tc} {maxpos} {COUNTS[maxpos]}')

    ### 런타임에러 ㅡㅡㅡㅡㅡㅡㅡㅡㅡ 왜

    # 테스트케이스 10개 중 5개 맞춤