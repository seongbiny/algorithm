'''
# 단어 하나하나씩 쭉 순회돌리면서 있으면 있는 곳의 인덱스를 반환
# 반환받은 인덱스들이 이어지는 숫자이면 1 출력
# => 실패
T =int(input())
for tc in range(1, T+1):
    n = list(map(str,input()))
    m = list(map(str,input()))
    result = []
    for i in range(len(n)):
        for j in range(len(m)):
            if n[i] is m[j]:
                result.append(j)
    print(result)
'''

# n 문자열을 m 문자열 0번부터 오른쪽으로 +1칸씩 옮겨가며 순회하다가
# 다 똑같은 곳이 있을때 1출력

T = int(input())
for tc in range(1, T+1):
    n = str(input())
    m = str(input())
    for i in range(len(n)):
        for j in range(len(m)):
            if 


