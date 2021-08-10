import sys
sys.stdin = open("input_flatten.txt","r")

for tc in range(1,11):
    dump = int(input())
    box = list(map(int,input().split()))

    maxV = 0
    minV = 100
    for i in box:
        if maxV < i:
            maxV = i
        if minV > i:
            minV = i
    max_idx = box.index(maxV)
    min_idx = box.index(minV)
    box[max_idx] -= 1
    box[min_idx] += 1
    dump -= 1
    print(f'#{tc} {maxV - minV}')
    '''
        while dump:
            max_box = max(box)
            min_box = min(box)
            max_idx = box.index(max(box))
            min_idx = box.index(min(box))

            box[max_idx] -= 1
            box[min_idx] += 1

            dump -= 1

        print(f'#{tc} {max(box)-min(box)}')
    '''
