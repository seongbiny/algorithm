T = int(input())
for tc in range(1, T+1):
    p, q = map(float, input().split())
    # p: 올바른 면 (1-p) : 뒤집어서
    # 올바른 면으로 꽂으면 q: 정상적 (1-q): 비정상 단, usb 뒤집어져있으면 안꽂힘
    # s1 = 1번 뒤집었을때 제대로 꽂힐 확률 s2 = 2번 뒤집었을때 제대로 꽂힐 확률
    # 1번 뒤집어서 꽂아서 맞을 확률 (1-p) * q
    # 처음 똑바로 비정상 p*(1-q)

    s1 = (1-p) * q
    s2 = p*(1-q)*q
    if s2 > s1:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')