n = int(input())
arr = [[0]*n for _ in range(n)]

word = 65
for i in range(n):
    while i != n:
        for j in range(n-1, i-1, -1):
            arr[i][j] = chr(word)
            word += 1
            i += 1
            if word > 90:
                word = 65

for i in range(n):
    result = ''
    for j in range(n):
        if arr[i][j] != 0:
            result += arr[i][j] + ' '
        elif arr[i][j] == 0:
            result += '  '
    print(result)