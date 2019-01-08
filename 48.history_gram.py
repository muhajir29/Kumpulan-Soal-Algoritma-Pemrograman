masukan = list(map(int, input().split()))
  
index = []
frekuensi= []  
for i in range(10):
    index.append(i)
  
    frekuensi.append(masukan.count(i))
  
for i in range(max(frekuensi), 0 , -1):
    for j in range(10):
        if i <= frekuensi[j]:
            print("\u2588", end="")
        else:
            print(" ", end="")
        if j == 9:
            print()
        else:
            print(end="  ")
 
strindex = []
strfrekuensi = []
  
for i in index:
    strindex.append(str(i))
for i in frekuensi:
    strfrekuensi.append(str(i))
  
print("  ".join(strindex))
print("  ".join(strfrekuensi))
