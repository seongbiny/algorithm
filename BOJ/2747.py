n = int(input())

result = [0, 1, 1]

for i in range(3, n+1):
    result.append(result[-1]+result[-2])

print(result[n])
