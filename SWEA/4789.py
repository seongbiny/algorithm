T = int(input())
for tc in range(1, T+1):
    lst = list(map(int,input()))
    # 문자열의 첫 번째 글자 = 기립 박수를 하고 있는 사람이 아무도 없을 때 기립 박수를 하는 사람의 수
    # i 번째 글자 = 기립 박수를 하고 있는 사람이 i-1명 이상일 때 기립박수를 하는 사람의 수
    clap = 0
    part_timer = 0
    clap += lst[0] # 1
    for i in range(1, len(lst)):
        if clap >= i:
            clap += lst[i]
        else:
            part_timer += (i - clap)
            clap += (i-clap) + lst[i]
    print(f'#{tc} {part_timer}')

