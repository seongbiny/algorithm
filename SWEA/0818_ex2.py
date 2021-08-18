s1 = '()()((()))'
s1 = '(()'
s1 = '())'

st = []
result = 'okay'
for c in s1:
    if c == '(':
        st.append(c)
    if c == ')':
        if len(st) == 0:
            result = 'error'
            break
        st.pop(-1)

if len(st) > 0:
    result = 'error'

print(result)