# str() 함수를 사용하지 않고, itoa()를 구현해보기
# 양의 정수를 입력 받아 문자열로 변환하는 함수
# 입력 값 : 변환할 정수 값, 변환된 문자열을 저장할 문자배열
# 반환 값 : 없음

'''
123 // 100 = 1
새로운 문자열 처음에 1 넣는다
123 % 10 = 3
새로운 문자열 맨 끝에 3 넣는다
(123 // 10)%10 = 2
새로운 문자열 가운데에 2 넣는다
입력받은 숫자 길이가 길어지면?  =>너무복잡

입력받은 int 를 하나씩 떼어 배열에 넣어주면 문자열이 된다 !
'''

word = int(input())

def itoa(num):
    new =[]
    while num > 0:
        a = num % 10
        new.append(a)
        num = num // 10
    return new[::-1]

if word < 0:
    word = -word

# 리스트를 문자열로.

result = ''.join(str(s) for s in itoa(word))
print(type(result))