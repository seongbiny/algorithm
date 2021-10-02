# A, 2~10, J, Q, K = 1~13

T = int(input())
for tc in range(1, T+1):
    card = list(input())
    S, D, H, C = 13, 13, 13, 13
    s_num = []
    d_num = []
    h_num = []
    c_num = []
    cnt = 0
    for i in range(0, len(card), 3):
        if card[i] == 'S':
            S -= 1
            new = int(card[i+1]+card[i+2])
            if new not in s_num[:-1]:
                s_num.append(new)
            else:
                cnt += 1
        elif card[i] == 'D':
            D -= 1
            new = int(card[i + 1] + card[i + 2])
            if new not in d_num[:-1]:
                d_num.append(new)
            else:
                cnt += 1
        elif card[i] == 'H':
            H -= 1
            new = int(card[i+1]+card[i+2])
            if new not in h_num[:-1]:
                h_num.append(new)
            else:
                cnt += 1
        elif card[i] == 'C':
            C -= 1
            new = int(card[i + 1] + card[i + 2])
            if new not in c_num[:-1]:
                c_num.append(new)
            else:
                cnt += 1
    if cnt == 0:
        print(f'#{tc} {S} {D} {H} {C}')
    else:
        print(f'#{tc} ERROR')



