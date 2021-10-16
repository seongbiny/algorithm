# def solve(left, right):
#     if left >= right:
#         return
#
#     global check, lst, result
#     mid = (left + right) // 2
#
#     for i in range(K):
#         check += lst[i] // mid
#
#     if check > N:
#         left = mid + 1
#         solve(left, right)
#     elif check < N:
#         right = mid - 1
#         solve(left, right)
#     else:
#         result = mid
#
#
K, N = map(int, input().split())
lst = []
for i in range(K):
    j = int(input())
    lst.append(j)
left, right = 1, max(lst)

while left <= right:
    mid = (left+right) // 2
    check = 0
    for i in lst:
        check += i//mid
    if check >= N:
        left = mid + 1
    else:
        right = mid - 1
    print(right)



