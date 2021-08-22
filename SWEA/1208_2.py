T = 10
for tc in range(1, 11):
    num = int(input())
    box = list(map(int, input().split()))

    for i in range(num):
        max_idx = box.index(max(box))
        min_idx = box.index(min(box))
        box[max_idx] -= 1
        box[min_idx] += 1
        