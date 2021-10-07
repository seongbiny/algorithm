def binary_search(lst, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, start, mid-1)
    else:
        return binary_search(lst, target, mid+1, end)

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
M = int(input())
array = list(map(int, input().split()))

for i in array:
    result = binary_search(lst, i, 0, N-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')