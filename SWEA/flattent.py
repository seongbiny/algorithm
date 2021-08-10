
def change():
    # h = getMaxPos() / getMaxValue()
    # l = getMin()
    # h를 기준으로 box하나 빼고 l을 기준으로 box를 하나 넣고

TC = 10
for tc in range(1, TC+1):
    dump = int(input())
    box = list(map(int,input().split()))

    for i in range(dump):
        change()

    result = 가장 높은 값 - 낮은 값

    print(f'#{tc} {result}')