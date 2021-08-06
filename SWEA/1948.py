T = int(input())
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1,T+1):
    sum1 = 0
    sum2 = 0
    m1,d1,m2,d2 = map(int,input().split())

    for j in range(0,m1-1):
            sum1 += day[j] # 앞 날짜의 총합
    for z in range(0,m2-1):
            sum2 += day[z] # 뒷 날짜의 총합
    
    sum1 = sum1 + d1
    sum2 = sum2 + d2

    print(f'#{i} {sum2-sum1+1}')