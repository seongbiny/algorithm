# 10진수 -> 2진수
def binary(num):
    binary = ''
    for i in range(3, -1, -1):
        binary += str(num // (2**i))
        num %= (2**i)
    return binary

# 16진수 -> 10진수
def decimal(str):
    if ord('0') <= ord(str) <= ord('9'):
        return ord(str) - ord('0')
    return ord(str) - ord('A') + 10

T = int(input())
for tc in range(1, T+1):
    n, hexadecimal = input().split()

    result = ''

    for i in hexadecimal:
        result += binary(decimal(i))

    print(f'#{tc} {result}')
