result = []

for i in range(9):
    num = int(input())
    result.append(num)

print(max(result))
print(result.index(max(result))+1)