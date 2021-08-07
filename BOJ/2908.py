'''
a,b = map(int,input().split())

num1 = []
num2 = []

for i in str(a):
    num1.append(i)
for j in str(b):
    num2.append(j)

num1 = ''.join(num1[::-1])
num2 = ''.join(num2[::-1])

if num1 > num2:
    print(num1)
else:
    print(num2)
'''

num1, num2 = input().split()
num1 = int(num1[::-1])
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else:
    print(num2)
