T = int(input())

for i in range(1,T+1):
    p, q, r, s, w = map(int,input().split())

    #A사 요금
    A = w*p
    #B사 요금
    if w <= r:
        B = q
    elif w > r:
        B = (q + (w-r)*s)

    #A, B 비교해서 더 적은 요금 출력
    if A >= B:
        print(f'#{i} {B}')
    else:
        print(f'#{i} {A}')
    