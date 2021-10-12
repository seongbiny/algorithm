def solve(idx, total):
    global N, B, result
    if idx == N:
        if total >= B and result > total - B:
            result = total - B
        return
    if total - B >= result:
        return
    solve(idx+1, H_lst[idx]+total)
    solve(idx+1, total)

T = int(input())
for tc in range(1, T+1):
    # 점원의 수, 탑의 높이
    N, B = map(int, input().split())
    # 점원들의 키
    H = list(map(int, input().split()))
    H_lst = sorted(H)
    # 최소값을 찾는거니까 큰 값으로 초기화 20 * 10000
    result = 200000

    solve(0, 0)

    print(f'#{tc} {result}')


# 모든 경우의 수를 구해보면 된다 -> DFS
# 최소 높이를 정했을 때 넘어가면 멈추도록 -> 백트래킹