def check(idx, taste, cal):
    global best_score
    if cal > L:
        return
    if taste > best_score:
        best_score = taste
    if idx == N:
        return
    check(idx+1, taste, cal) # 재료 X
    check(idx+1, taste+taste_lst[idx], cal+cal_lst[idx]) # 재료 O

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    taste_lst = []
    cal_lst = []
    for i in range(N):
        T, K = map(int, input().split())
        taste_lst.append(T)
        cal_lst.append(K)
    best_score = 0
    check(0,0,0)
    print(f'#{tc} {best_score}')

