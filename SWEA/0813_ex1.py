# join 제외 사용 금지
# 문자열 받고 새로운 문자열 t를 만들고 return t
# 리버스시켜주는 함수 만든다.
# 테스트 할때는 기본 문자열s 에다가 t = myrevers(s) print t

word = input()

def reverse(a):
    return a[::-1]

t = reverse(word)
print(t)