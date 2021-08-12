'''
1. 숫자와 기호를 나눠서 표기한다.
2. 숫자 중 최소 2개와 기호 중 최소 1개를 뽑아서 부분집합 만든다.
3. 기호는 홀수번째 인덱스, 숫자는 짝수번째 인덱스
'''

#form = input().split('+' or '-')
#print(form)

form1 = ['55', '-', '50', '+', '40']
num = ['55', '50', '40']
sign = ['-', '+']

n = len(num)
for i in range(1<<n):
    for j in range(n+1): # 0 1 2
        if i | (1<<j) != True:
            print(num[j])
    #print()

