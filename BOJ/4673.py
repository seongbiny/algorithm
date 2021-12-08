def self_num(num):
    if len(str(num)) == 1:
        return num+num
    elif len(str(num)) == 2:
        return num + num%10 + num//10
    elif len(str(num)) == 3:
        a = num + num%10 + num//100 + (num//10)%10
        return a
    elif len(str(num)) == 4:
        a = num + num // 1000 + (num // 100) % 10 + (num // 10) % 10 + num % 10
        return a

result = []
for i in range(1, 10001):
    result.append(self_num(i))
    if i not in result:
        print(i)