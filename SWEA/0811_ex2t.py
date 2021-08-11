#import sys
#sys.stdin = open("in2.txt","r")

# 0b11111 (= 2^6-1), 2^6
lst = [-7, -5, -2, 5 , 8]

# 0 & 0 : 0
# 0 & 1 : 0
# 1 & 0 : 0
# 1 & 1 : 1

#i = 12 #0b01100  # 뒤집혀서 끝에서부터 출력된다
#제일 끝의 bit를 확인하자
#i & 0b00001 => 00000/00001
# 끝에서 두번째 bit 확인
#i & 0b00010 => 00000/00010

N = len(lst)
for i in range(1<<N):  #0b11111 + 1 = 0b100000 = 1<<5
    sumV = 0
    for j in range(N): # bit 수 만큼 돌려
        r = i & (1<<j)
        if r != 0:
            sumV += lst[j]
            print('1', end='')
        else:
            print('0', end='')
    print()
    print(i, sumV)