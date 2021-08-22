T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    max_sum = 0
    min_sum = 999999999 # 임의의 큰값
    result = 0
    for i in range(n-m+1):
        sum_num = 0 # 구간 합
        for j in range(m):
            sum_num += num[i+j] # 구간 안의 합
        if sum_num > max_sum: # 최대 합 구간 갱신
            max_sum = sum_num
        if sum_num < min_sum: # 최소 합 구간 갱신
            min_sum = sum_num

    result = max_sum - min_sum
