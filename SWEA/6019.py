T = int(input())
for tc in range(1, T+1):
    d, a, b, f = map(int, input().split())
    # d 두 기차 전면부 사이의 거리
    # a 기차 a의 속력
    # b 기차 b의 속력
    # f 파리의 속력

    time_1 = d / (f + b) # 파리 기차b 충돌하기까지 걸린 시간
    length = time_1 * (f - a) # 그 시간에 기차a와 기차b 사이 남은 거리
    time_2 = length / (a + b) # 그 남은 거리를 기차 a와 기차b가 부딪히기까지 시간

    total = f * (time_1 + time_2)

    print(f'#{tc} {total}')


