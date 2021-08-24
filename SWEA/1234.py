T = 10
for tc in range(1, 11):
    length, nums = map(str, input().split())
    arr = []
    st = []
    for i in nums:
        arr.append(i)
    #print(arr)
    for i in range(len(nums)): # 0 1 2 3 4 .. 9
        if len(st) == 0:
            st.append(arr[i])
        else:
            st.append(arr[i])
            if st[-2] == st[-1]:
                st.pop(-1)
                st.pop(-1)


    print(f'#{tc} {"".join(st)}')
