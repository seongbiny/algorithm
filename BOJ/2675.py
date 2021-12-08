t = int(input())
for _ in range(t):
    r, s = map(str, input().split())
    r = int(r)

    for i in range(len(s)):
        print(r*s[i], end='')
    print()