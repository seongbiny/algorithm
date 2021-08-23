s = input()
st = []
result = ''
for c in s:
    if c == '+' or c =='-' or c == '*' or c =='/':
        st.append(c)
    else:
        result += c

for i in range(len(st)):
    result += st.pop()
# while st:
#     print(st.pop(-1))
print(result)


# for c in s:
#     # 방법1
#     if c in ['+', '-', '*', '/']:
#         st.append(c)
#     else:
#         print(c)
#
#     # 방법2
#     if c.isdecimal():
#         print(c)
#     else:
#         st.append(c)
