n = int(input())
yist = []
for i in range(n):
    masukan = list(map(int, input().split()))
    yist.append(masukan)
 
 
move = input()
nilai = []
biner = 1
if move[0] == "B":
 
    yist.reverse()
for i in yist:
    if move[0] == "F":
        if move[1]== "R":
            nilai.append(i[biner])
        else:
            nilai.append(i[biner-1])
    else:
        if move[1]== "R":
            nilai.append(i[biner])
        else:
            nilai.append(i[biner-1])
    if biner == 1:
        biner = 0
    else:
        biner = 1
strnilai = []
for i in nilai:
    strnilai.append(str(i))
 
print(" ".join(strnilai))
