T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    mid_idx = n//2
    total = 0

    for r in range(mid_idx+1):
        i = r
        while i < r+1:
            total += sum(arr[r][mid_idx-i:mid_idx+i+1])
            i += 1
    for r in range(mid_idx+1, n):
        j = r
        while j < r+1:
            total += sum(arr[r][j-mid_idx:-(j-mid_idx)])
            j += 1

    print(f'#{tc} {total}')