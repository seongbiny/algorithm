n, m = map(int, input().split())
if n > 100:
    print("INPUT ERROR!")
if m == 1:
    for i in range(1, n+1):
        print('*'*i)
elif m == 2:
    for j in range(n, 0, -1):
        print('*'*j)
elif m == 3:
    pass