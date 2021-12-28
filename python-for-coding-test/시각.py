n = int(input())

cnt = 0

for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            if '3' in str(h) or '3' in str(m) or '3' in str(s):
                cnt += 1

print(cnt)

