import sys
sys.stdin = open("input_flatten.txt","r")

def bubble(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

for tc in range(1,11):
    dump = int(input())
    box = list(map(int,input().split()))

    for z in range(dump):
        bubble(box)
        box[0] += 1
        box[-1] -= 1
    bubble(box)

    print(f'#{tc} {box[-1]-box[0]}')


