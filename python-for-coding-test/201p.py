N, M = map(int, input().split())
ricecake = list(map(int, input().split()))

start = 0
end = max(ricecake)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in ricecake:
        if x > mid:
            total += x - mid
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)