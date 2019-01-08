'''
CEK TINGGI
pak amru secara rutin memeriksa barisan para siswa sebelum memasuki kelas.
baris harus tersusun berdasarkan tinggi dengan siswa paling pendek di awal dan siswa paling tinggi di akhir.
agar barisan terlihat rapi, pak amru ingin selisih tinggi seorang siswa dengan yang di depannya tidak
melebihi batas tertentu

FORMAT MASUKAN
barisan pertama berisikan suatu integer, n, yakni banyaknya siswa yang akan berbaris.
sebanyak n baris berikut berisikan tinggi masing- masing siswa . baris berikutnya berisi batas selisih yang diizinkan..

FORMAT KELUARAN
sebuah bilangan bulat yang merupakan banyaknya siswa yang setelah berbaris tenyata melebihi
di posisi yang keliru . keluaran diakhiri newline

CONTOH MASUKAN
5
160
170
168
158
165
2

CONTOH KELUARAN
2

'''
n = int(input())
data = []
for i in range(n):
    tinggi = int(input())
    data.append(tinggi)
data.sort()
batas = int(input())
nilaisalah = 0
for j in range(len(data)-1):
    if (data[j+1]- data[j]) > batas:
        nilaisalah +=1
print(nilaisalah)

