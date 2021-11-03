import sys
input = sys.stdin.readline

sik = list(map(str, input()))
st = []
result = ''
operator = ['+', '/', '*', '-']

for i in sik:
    # 알파벳일때
    if i.isalpha():
        result += i
    # 알파벳이 아닐때
    elif (i in operator) or (i == '(') or (i == ')'):
        if not st:
            st.append(i)
        elif i == '+' or i == '-':
            while st and st[-1] != '(':
                result += st.pop()
            st.append(i)
        elif i == '*' or i == '/':
            if st[-1] == '+' or st[-1] == '-':
                st.append(i)
            else:
                result += st.pop()
                st.append(i)
        elif i == '(':
            st.append(i)
        elif i == ')':
            while True:
                if st and st[-1] != '(':
                    result += st.pop()
                else:
                    st.pop()
                    break

while st:
    result += st.pop()

print(result)






