# 비트 사용하지말고 부분집합 직접 만들어봐

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12]
    bits = 12 # 비트수 나올 수 있는 부분집합이 0b000000000000 ~ 0b111111111111
    #101101111111 {1, 2, 3, 4, 5, 6, 7, 9, 10, 12}
    result = 0
    for i in range(1<<12): #12 = bits #0b11111111111 + 1 을 범위에 넣는다 => 1<<12
        sumV = 0
        cnt = 0
        #print(i, end='=>')
        for j in range(bits):
            if i & (1<<j):
                #print(lst[j], end=' ') #i별로 한줄로 찍어본다
                sumV += lst[j]
                cnt += 1 # 원소의 갯수를 세라
        #print()
        #print(i, cnt, sumV)

        # cnt 가 n 이고 sumV 가 k 인 갯수를 출력하라
        if cnt == n and sumV == k:
            result += 1

    print(f'#{tc} {result}')