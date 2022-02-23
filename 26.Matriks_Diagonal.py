'''
 Create 26.Matriks_Diagonal.py

Buatlah program yang dapat menghasilkan matriks persegi diagonal berukuran n x n.
Diagonal dari matriks diisi dengan angka-angka yang diberikan sebagai input,
sedangkan sisanya diisi nol.

Format Masukan
Masukan terdiri atas dua baris. Baris pertama adalah n, yaitu ukuran baris dan kolom matriks (1 <= n <= 100).
Baris kedua adalah angka-angka sebanyak n, dengan masing-masing angka dalam rentang 0 <= x <= 9.

Format Keluaran
Keluaran adalah matriks berukuran n x n sesuai ketentuan. Setiap elemen matriks dipisahkan dengan satu spasi, 
kecuali kolom terakhir yang langsung berupa newline tanpa spasi.

Contoh Masukan 1
1
7

Contoh Keluaran 1
7

Contoh Masukan 2
10
0 7 6 2 5 0 3 5 9 7

Contoh Keluaran 2
0 0 0 0 0 0 0 0 0 0
0 7 0 0 0 0 0 0 0 0
0 0 6 0 0 0 0 0 0 0
0 0 0 2 0 0 0 0 0 0
0 0 0 0 5 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 3 0 0 0
0 0 0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0 9 0
0 0 0 0 0 0 0 0 0 7

'''


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
