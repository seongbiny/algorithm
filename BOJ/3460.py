t = int(input())
for i in range(t):
    num = int(input())
    lst = []
    while num > 0:
        lst.insert(0, num % 2)
        num = num // 2

    for idx in range(len(lst)):
        if lst[-idx-1] == 1:
            print(idx, end=" ")



# 13
# 17
# 8 1
# 4 0
# 2 0
# 1 0