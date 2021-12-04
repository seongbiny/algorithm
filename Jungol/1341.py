while True:
    s, e = map(int, input().split())
    if s < e and 2 <= s <= 9 and 2 <= e <= 9:
        for i in range(s, e + 1):
            for j in range(1, 10):
                if j % 3 == 0 and i * j < 10:
                    print(f'{i} * {j} =  {i * j}')
                elif i * j < 10:
                    print(f'{i} * {j} =  {i * j}', end="   ")
                elif j % 3 == 0:
                    print(f'{i} * {j} = {i * j}')
                else:
                    print(f'{i} * {j} = {i * j}', end="   ")
            print()

    elif s >= e and 2 <= s <= 9 and 2 <= e <= 9:
        for i in range(s, e-1, -1):
            for j in range(1, 10):
                if j % 3 == 0 and i*j < 10:
                    print(f'{i} * {j} =  {i*j}')
                elif i*j < 10:
                    print(f'{i} * {j} =  {i*j}', end="   ")
                elif j % 3 == 0:
                    print(f'{i} * {j} = {i*j}')
                else:
                    print(f'{i} * {j} = {i*j}', end="   ")
            print()

