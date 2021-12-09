n = int(input())
result = 0
for i in range(n):
    word = input()
    lst = []
    cnt = 0
    for j in word:
        if j not in lst or lst[-1] == j:
            lst.append(j)
            cnt += 1
        else:
            cnt = 0

    if cnt == len(word):
        result += 1

print(result)

