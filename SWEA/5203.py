def check(cnt):
    if len(cnt) < 3:
        return 0
    else:
        for i in range(10):
            if cnt[i] >= 3:
                return 1
            if i <= 7 and cnt[i] and cnt[i+1] and cnt[i+2]: # 0이 아니면 ~
                return 1

T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))

    player1 = [0] * 10
    player2 = [0] * 10
    win = 0

    for i in range(0, 12, 2):
        player1[card[i]] += 1
        player2[card[i+1]] += 1
        # p1에 대해 run/tri 체크
        if check(player1):
            win = 1
            break
        # p2에 대해 run/tri 체크
        if check(player2):
            win = 2
            break

    print(f'#{tc} {win}')







