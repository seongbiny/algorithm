N, M = map(int, input().split())
if M == 1:
    for i in range(1,7):
        for j in range(1, 7):
            for k in range(1, 7):
                print(i, j, k)
result = []
if M == 2:
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                a = sorted([i, j, k])
                if a not in result:
                    result.append([i, j, k])
                    print(i, j, k)
if M == 3:
    for i in range(1, 7):
        for j in range(1, 7):
            if j == i:
                break
            else:
                for k in range(1, 7):
                    if k != j and k != i:
                        print(i, j, k)