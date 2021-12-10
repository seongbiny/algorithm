t = int(input())
for i in range(t):
    num = int(input())
    lst = []
    while num > 2:
        lst.append(num % 2)
        num = num // 2
        if num == 1:
            lst.append(1)
    print(lst)
    for idx in range(len(lst)):
        if lst[idx] == 1:
            print(idx, end=" ")



# 13
# 6 1
# 3 0
# 1 1
# 1 0 1 1