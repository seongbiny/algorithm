T = int(input())
for tc in range(1, T+1):
    d, h, m = map(int, input().split())

    # 2011년 11월 11일 오전 11시 11분 분 단위 출력
    # 1일 = 60*24 분
    # 11 <= d <= 14 d, h, m 만 계산

    total = 11 * (60 * 24) + 11 * 60 + 11
    wait = d * (60 * 24) + h * 60 + m

    if total <= wait:
        result = wait - total
    else:
        result = -1

    print(f'#{tc} {result}')




