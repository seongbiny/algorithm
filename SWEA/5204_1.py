def merge(left, right):
    global cnt
    # merge 리스트 담을 곳
    lst = [0] * (len(left) + len(right))

    left_idx = 0
    right_idx = 0
    i = 0

    if left[-1] > right[-1]:
        cnt += 1

    while left_idx < len(left) or right_idx < len(right):
        if left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                lst[i] = left[left_idx]
                i += 1
                left_idx += 1
            else:
                lst[i] = right[right_idx]
                i += 1
                right_idx += 1
        elif left_idx < len(left):
            lst[i] = left[left_idx]
            i += 1
            left_idx += 1
        elif right_idx < len(right):
            lst[i] = right[right_idx]
            i += 1
            right_idx += 1
    return lst

def partition(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = partition(arr[:mid])
    right = partition(arr[mid:])

    return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = partition(arr)

    print(f'#{tc} {result[N//2]} {cnt}')