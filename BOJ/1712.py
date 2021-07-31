a, b, c = map(int,input().split())


if b >= c:
    print(-1)
else:
    q = a/(c-b)
    q = q +1
    print(int(q))