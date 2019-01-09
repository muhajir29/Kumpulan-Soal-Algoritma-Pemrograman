n = int(input())
 
# 00 01 02 03 04
# 10 11 12 13 14
# 20 21 22 23 24
# 30 31 32 33 34
# 40 41 42 43 44
 
a = int(n/2)
b = int(n/2)
 
for i in range(n):
    for j in range(n):
        if j == a or j ==b:
            print('_', end='')
        else:
            print(" ",end="")
 
    if i < int(n/2):
        a = a + 1
        b = b - 1
    else:
        a = a - 1
        b = b + 1
 
    print()
