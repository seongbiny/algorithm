T = int(input())
for tc in range(1, T+1):
    word = list(input())
    #l = len(word)
    h = int(input()) # 넣을 하이픈의 갯수
    lo = list(map(int, input().split())) # 2 3 2
    # j = 0
    # for i in range(len(lo)):
    #     word.insert(lo[i]+j, '-')
    #     j = 1
    # print(f'#{tc} {"".join(word)}')
    lo = sorted(lo, reverse=True) # 3 2 2

    for i in lo:
        word.insert(i, '-')
    print(f"#{tc} {''.join(word)}")


