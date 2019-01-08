'''
CEK SISI KIRI
pak budi membuat sebuah program untuk mengurutkan daftar bilangan bulat.
salah satu langkahnya ialah memastikan seluruh bilangan diparuh kiri lebih kecil atau sama dengan dari seluruh bilangan
dari paruh kanan . Bantulah pak budi untuk mengecek sisi kiri dan mengenali banyaknya bilangan yang salah posisi.
jika banyaknya bilangan bersifat ganjil , bilangan di tengah- tengah daftar dimasuakn ke sisi kanan

FORMAT MASUKAN
Daftar  bilangan bulat dari yang paling kiri hingga paling dengan tiap baris berisikan sebuah bilangan.
akhir data ditandai oleh suatu baris berisikan karakter titik.

FORMAT KELUARAN
banyaknya bilangan di sisi kiri yang tidak memenuhi kriteria.
keluaran akhir nweline

CONTOH MASUKAN
3
5
7
5
6
5
8
10
9
.

CONTOH KELUARAN
1

'''
angka = int(input())
a = 0
data=[]
while angka != '.':
    if angka != '.':
        stra = int(angka)
        data.append(stra)
        angka = str(input())
        a += 1
setengahdata = data[:(a//2)]
salah = 0
for i in range(len(setengahdata)-1):
    if setengahdata[i+1] < setengahdata[i]:
        salah +=1
print(salah)

