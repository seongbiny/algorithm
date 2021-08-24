a = int(input())
price = 1000 - a
charge = [500, 100, 50, 10, 5, 1]
cnt = [0] * 6

for i in range(len(charge)):
    if price//charge[i] != 0:
        cnt[i] += price//charge[i]
        price -= cnt[i] * charge[i]

print(sum(cnt))


