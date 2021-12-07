T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = []
    for i in range(n):
        name, category = map(str, input().split())
        lst.append(category)

    category = tuple(set(lst))

    wear = []
    for i in range(len(category)):
        wear.append(lst.count(category[i]))

    result = 1
    for i in wear:
        result = result * (i + 1)

    print(result - 1)

