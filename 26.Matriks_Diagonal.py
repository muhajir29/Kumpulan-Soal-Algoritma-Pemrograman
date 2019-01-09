x =  int(input())
masuk = list(map(int, input().split()))
 
for i in range(x):
    for j in range(x):
        if i==j:
            print(masuk[i],end="")
        else:
            print('0', end="")
        if j < x-1:
            print(' ',end='')
        else:
            print()
