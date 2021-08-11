'''
1. 단어 입력받기
2. 단어 제일 끝 문자열부터 하나씩 빼주고
2-1. 문자열 길이를 조절해서 출력하기
2-2. 포문으로 문자열 제일 끝 단어를 뽑아내서 주어진 문자열에서 지우기?
3. 나머지 단어 출력
4. 그렇게 하나씩 빼가며 출력한 단어들을 리스트에 담고
5. 정렬한다.
'''

word = str(input())
lst = []
result = []
for i in range(1,len(word)+1): # 1 2 3 ..
    lst.append(word[-i:])
    for j in range(len(lst)-1, 0, -1):
        for z in range(0, j):
            if lst[z] > lst[z+1]:
                lst[z], lst[z+1] = lst[z+1], lst[z]
for k in lst:
    print(k)


