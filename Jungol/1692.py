num1 = int(input())
num2 = list(map(int, input()))

print(num1*num2[2])
print(num1*num2[1])
print(num1*num2[0])

for i in range(3):
    num2[i] = str(num2[i])
num3 = "".join(num2)
num3 = int(num3)

print(num1*num3)