n, m = map(int, input().split())

n_arr = []
m_arr = []

for i in range(n):
    a = input()
    n_arr.append(a)
for i in range(m):
    b = input()
    m_arr.append(b)


result = list(set(m_arr).intersection(n_arr))
result_n = sorted(result)
# print(result)
print(len(result_n))
print("\n".join(result_n))




