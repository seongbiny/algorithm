a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
burger = []
drink = []
result = []

burger.append(a)
burger.append(b)
burger.append(c)
drink.append(d)
drink.append(e)

for i in burger:
    for j in drink:
        result.append(i + j - 50)

print(min(result))
