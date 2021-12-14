from sys import stdin, stdout
input = stdin.readline

arr = [list(map(int, input().split())) for _ in range(10)]

person = 0
maxV = 0
for i in range(10):
    person += arr[i][1]
    person -= arr[i][0]
    if person > maxV:
        maxV = person

print(maxV)
