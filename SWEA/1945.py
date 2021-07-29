
N = int(input()) # 테스트 케이스 갯수 입력 받음

for i in range(N): # 테스트 케이스 갯수만큼 for문을 돌릴 것임
    num = int(input()) # num은 2 이상 10,000,000 이하이다.
    a_cnt = 0; b_cnt = 0; c_cnt = 0; d_cnt = 0; e_cnt = 0
   
    while num != 1:
    #while num != 1:
        if num % 2 == 0:
            a_cnt += 1
            num = num//2
    
        elif num % 3 == 0:
            b_cnt += 1
            num = num//3
            
        elif num % 5 == 0:
            c_cnt += 1
            num = num//5

        elif num % 7 == 0:
            d_cnt += 1
            num = num//7

        elif num % 11 == 0:
            e_cnt += 1
            num = num//11
            

    print(f'#{i+1} {a_cnt} {b_cnt} {c_cnt} {d_cnt} {e_cnt}')
