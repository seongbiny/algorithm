
for i in range(3):
    a, b, c, d = map(int,input().split())
    result = []
    result.append(a)
    result.append(b)
    result.append(c)
    result.append(d)

    if result.count(0) == 1 and result.count(1) == 3:
        print('A')
    elif result.count(0) == 2 and result.count(1) == 2:
        print('B')
    elif result.count(0) == 3 and result.count(1) == 1:
        print('C')
    elif result.count(0) == 4:
        print('D')
    elif result.count(1) == 4:
        print('E')


