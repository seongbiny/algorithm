# 셀렉션 정렬
#짝수일때는 제일 큰 값을 구해서 앞에 넣고
#홀수일때는 제일 작은 값을 해서 앞에 넣는다.
'''
0번째는 [0..N-1] 가장 큰 값을 구해서 0번째의 데이터와 교환
1번째는 [1..N-1] 가장 작은 값을 구해서 1번째의 데이터와 교환
2번째는 [2..N-1] 가장 큰 값을 구해서 2번째의 데이터와 교환

i번째는 [i..N-1] i가 짝수일대는 가장 큰값을, 홀수일때는 가장 작은값
for i range( ):
    if i가 짝수일때
        for j in range(i, N)
            maxV ...
        i번째 데이터와 maxV가 있는 위치의 데이터와 교환

    else: #i가 홀수일때
        for j in range(i, N)
'''
def getMaxPos(lst):
    maxP = 0
    n = len(lst)
    for j in range(1, n):
        if ai[maxP] < ai[j]:
            # maxV = ai[j]
            maxP = j
    return maxP

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ai = list(map(int,input().split()))

i = 0일때는 [0:N-1] 중에서 max
i = 1일때는 [1:N-1] 중에서 min
i = 2일때는 [2:N-1] 중에서 max

i번째는 [i:N-1] 중에서 짝 맥 홀 민

    for i in range(0, n-1): # 맨 마지막은 안 구해도 되니까
        if i%2 == 0: #i 가 짝수일때 :
            maxP = getMaxPos(ai[i:]) #범위를 잘라서 함수로 보내줘야함
            #maxV = ai[i]
            #maxP = 0
            #for j in range(i+1, n): #함수로 뽑으면 영역이 달라짐!!
            #    if ai[maxP] < ai[j]:
                    #maxV = ai[j]
            #        maxP = j
    #i번째 위치에 있는 값과 구한 최대값을 교환
            ai[maxP], ai[i] = ai[i], ai[maxP]
        else:
            minP = 0
            for j in range(i+1, n):
                if ai[minP] > ai[j]:
                    minP = j
            ai[minP], ai[i] = ai[i], ai[minP]
    print(제목, end=' ')
    for i in range(10):
        print(ai[i], end = ' ')
    print()
