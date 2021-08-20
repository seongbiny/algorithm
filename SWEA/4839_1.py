T = int(input())
for tc in range(1, T+1):
    p, pa, pb = map(int, input().split())
    result = []
    lst = []
    lst.append(pa)
    lst.append(pb)

    for i in range(2): # 0 1
        start = 1
        end = p
        cnt = 0
        middle = (start + end) // 2
        while middle != lst[i]:
            if middle == lst[i]:
                cnt += 1
            elif middle > lst[i]:
                end = middle
                cnt += 1
            else:
                start = middle
                cnt += 1
            middle = (start+end)//2
        result.append(cnt)

    if result[0] > result[1]:
        print(f'#{tc} B')
    elif result[0] == result[1]:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} A')


