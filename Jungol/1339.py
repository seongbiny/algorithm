n = int(input())
arr = [[0]*n for _ in range(n)]

word = 65
arr[n//2][n//2] = chr(word)

for i in range((n//2)-1, n):
    for j in range((n//2)-1, -1, -1):