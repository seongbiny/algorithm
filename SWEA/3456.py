T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))

    if lst.count(lst[0]) == 3:
        print(f'#{tc} {lst[0]}')

    for i in range(3):
        if lst.count(lst[i]) == 1:
            print(f'#{tc} {lst[i]}')
