T = int(input())
for tc in range(1, T+1):
    h1,m1,h2,m2 = map(int,input().split())

    #print(h1,m1,h2,m2)
    result = []

    newh = 0
    newm = 0

    newh = h1 + h2
    newm = m1 + m2
    if newm > 60:
        newh += 1
        newm -= 60
    if newh > 12:
        newh -= 12
    #result.append(newh)
    #result.append(newm)
    #print(result)
    #a = ' '.join(map(str, result))

    print(f'#{tc} {newh} {newm}')

