# a = [20, 31, 78]
# t = [False] * 3
#
# def powerset(k):
#     if k == 3:
#         print(t, end= ' ')
#         for i in range(len(t)):
#             if t[i]:
#                 print(a[i], end=' ')
#         print()
#
#     else:
#         t[k] = True
#         powerset(k+1)
#         t[k] = False
#         powerset(k+1)
#
#
# powerset(0)

a = [20, 31, 78]
t = [False] * 3

def powerset(k):
    if k == 3:
        print(t, end= ' ')
        for i in range(len(t)):
            if t[i]:
                print(a[i], end=' ')
        print()

    else:
        for i in range(2): # 0 1
            t[k] = i
            powerset(k+1)

powerset(0)