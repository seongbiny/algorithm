T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    lst.remove(max(lst))
    lst.remove(min(lst))
    result = sum(lst) / len(lst)
    print(f'#{tc} {round(result)}')