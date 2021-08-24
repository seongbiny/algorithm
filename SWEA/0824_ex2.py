a = [20, 31, 78]
t = [0] * 3



def powerset(k, input, sumV):
    if sumV > 10:
        return

    if k == input:
        #print(t, end= ' ')
        # sumV = 0
        # for i in range(3):
        #     if t[i]:
        #         sumV += a[i]
        #         #print(a[i], end=' ')

        if sumV == 10:
            for i in range(3):
                if t[i]:
                    print(a[i], end=' ')
        print()
    else:
        t[k] = True
        powerset(k+1, input, sumV + a[k])
        t[k] = False
        powerset(k+1, input, sumV)
        # for i in range(2):
        #     t[k] = i
        #     powerset(k+1)

powerset(0, 10, 0)

def per(k):
    if k == 3:
