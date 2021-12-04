while True:
    s, e = map(int, input().split())
    if s <= e and 2 <= s <= 9 and 2 <= e <= 9:
        for i in range(1, 10):
            for j in range(s, e+1):
                if j * i < 10:
                    print(f'{j} * {i} =  {i * j}', end="   ")
                else:
                    print(f'{j} * {i} = {i * j}', end="   ")
            print()

    elif s > e and 2 <= s <= 9 and 2 <= e <= 9:
        for i in range(1, 10):
            for j in range(s, e-1, -1):
                if j*i < 10:
                    print(f'{j} * {i} =  {i * j}', end="   ")
                else:
                    print(f'{j} * {i} = {i * j}', end="   ")
            print()

    else:
        print("INPUT ERROR!")

