
def pattern_B(P):
    lenT = len(T)
    lenP = len(P)

    for idxT in range(lenT - lenP): #범위 생각해봐
        #T의 스타트 위치
        #for j in range(lenP): #for 를 쓰면 중간에 나올때 브렠 걸어줘야함
        idxP = 0
        while idxP < lenP and P[idxP] == T[   ]: #idxP가 무한히 돌고있다. 종료조건 넣어
            idxP += 1
        if idxP == lenP: # 찾았다는 조건
            return idxT
        else:
            idxT += 1
    return -1

T = "TTTTAACCABCDEFTTATTTF"
#P = "TTATTT"

result = pattern_B('TTATTT')
print(result)
print(pattern_B('TTABC'))

def pattern_BMOOR(P):
    lenT = len(T)
    lenP = len(P)

    #배열 만들어
    jumpA = [lenP] * 128 #문자열 총 128개
    value = 0
    for i in range(lenP-1, -1, -1):
        c = P[i]
        jumpA[ord(P[i])] = value
        value += 1

    while idxT < #포문은 별로 하나씩 가는게 아니라 스킵하는거니까
        idxP = 마지막위치
        #lsatT = #마지막 텍스트 위치
        #거꾸로 역으로 비교한다.
        while idxP < lenP and P[idxP] == T[   ]: #idxP가 무한히 돌고있다. 종료조건 넣어
            idxP += 1
        if idxP == lenP: # 찾았다는 조건
            return
        else:
            jump
    return -1

