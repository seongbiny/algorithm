def dfs(idx):
    global charge, result
    if idx >= N:
        if result >= charge:
            result = charge
            return
    if result <= charge:
        return

    for i in range(idx+lst[idx], idx, -1):
        charge += 1
        dfs(i)
        charge -= 1

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))

    N = lst[0]
    result = 999999
    charge = 0
    dfs(1)

    print(f'#{tc} {result-1}')