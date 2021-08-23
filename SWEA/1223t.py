def step1(s):
    isp = {'*': 2, '+': 1}
    t = []
    st = []
    for c in s:
        if c.isdecimal():
            t.append(c)
        else:
            if len(st) == 0 or isp[st[-1]] < isp[c]:
                st.append(c)
            else:
                while st and isp[st[-1]] >= isp[c]:
                    t.append(st.pop())
    while st:
        t.append(st.pop(-1))
    return t

def step2(t):
    st = []
    for c in t:
        if c.isdecimal():
            st.append(c)
        else:
            n1 = st.pop()
            n2 = st.pop()
            if c == '+':
                st.append(n1+n2)
            if c == '*':
                st.append(n1*n2)
    return st.pop()

T = 10
for tc in range(1, T+1):
    n = int(input())
    s = input()
    result = step2(step1(s))




