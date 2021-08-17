while j<M and i<n:
    if t[i] == p[j]:
        i += 1
        j += 1
    else:
        i = i - j + 1
        j = 0

=> for i < n-M+1:
    while j < M and p[j] == T[i]:
        j += 1
    if j == M: