a, b = map(int,input().split())
print(a+b)

# input 한 번에 값을 여러 개 입력받을 때 split 사용
'''
변수1, 변수2 = map(input().split())
변수1, 변수2 = map(input().split('기준문자열'))
변수1, 변수2 = map(input('문자열').split())
변수1, 변수2 = map(input('문자열').split('기준문자열'))
'''
# map()함수는 여러개의 data를 한번에 다른 형태로 변환시켜준다.