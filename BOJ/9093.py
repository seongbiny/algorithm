t = int(input())
for tc in range(t):
    sentence = list(map(str, input().split()))
    for i in sentence:
        print(i[::-1], end=" ")