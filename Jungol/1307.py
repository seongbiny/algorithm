n = int(input())
arr = [[0]*n for _ in range(n)]

word = 65
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        arr[j][i] = chr(word)
        word += 1
        if word > 90:
            word = 65

for i in range(n):
    result = ''
    for j in range(n):
        result += arr[i][j] + ' '
    print(result)

