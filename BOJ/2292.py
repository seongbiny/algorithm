lst = [[1]]

def solve(num):
    for i in range(6, 1000000001, 6):
        a = []
        for j in range(i, i+7):
            a.append(j)
        lst.append(a)


n = int(input())
for i in range(len(lst)):
    if n in lst[i]:
        print(i)
