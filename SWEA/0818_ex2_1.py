def F_2():
    print('2_1')   #5
    print('2_2')   #6
    return         #7

def F_1():
    print('1_1')    #3     #13
    F_2()           #4, #8
    print('1_2')    #9
    return          #10

print('1')       #1
F_1()            #2
print('2')       #11

F_1()            #12
print('3')