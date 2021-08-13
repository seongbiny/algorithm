'''
문자열을 다 입력받아.
zro = 0
one = 1
..
할당해줘
할당된 숫자들을 오름차순으로 정렬해줘
숫자를 다시 문자열로 반환
'''
import sys
sys.stdin = open("GNS_test_input.txt","r")

T = int(input())
for tc in range(1, T+1):
    num = input().split()
    a = int(num[1])
    nums = list(map(str, input().split()))

    dict = { 'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9 }

    for i in range(len(nums)):
        if nums[i] in dict.keys():
            nums[i] = dict[nums[i]]

    for j in range(len(nums)-1, 0, -1):
        for z in range(0, j):
            if nums[z] > nums[z+1]:
                nums[z], nums[z+1] = nums[z+1], nums[z]
    '''
    #print(nums)
    new = []
    # 값으로 키 값 찾아서 키로 다시 반환해주기
    for k in range(len(nums)):
        #nums[k] = dict.get(str(nums[k]))
        #new.append(dict.get(str(nums[k])))
        #print(nums[k], type(nums[k]))
        #print()
    '''
    new_dict = {v:k for k, v in dict.items()} # 딕셔너리 키와 값 자리 변경해주는거

    for k in range(len(nums)):
        nums[k] = new_dict.get(nums[k])
    print(f'#{tc}')
    print(' '.join(nums))

