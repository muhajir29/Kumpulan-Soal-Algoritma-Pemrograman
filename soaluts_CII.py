'''
VALIDASI DATA

pak bayu membacakan sekumpulan data dalam rentang [100, 9 999 999] melalui telepon.
Digit terakhir data menunjukan banyaknya digit sebelumnya.
Digit terakhir = 0 jijka panjang data sebelumnya genap dan 1 jika panjang data sebelumnya ganjil.
anda ditugaskan untuk menghitunga banyaknya data yang tidak valid

FORMAT MASUKAN
baris pertama memuat suatu bilangan bulat, n, diikuti n baris yang merupakan data yang dibacakan

FORMAT KELUARAN
sebuah bilangan bulat yang merupakan banyaknya data yang tidak valid. keluaran diakhiri newline

CONTOH MASUKAN
5
5641
340
27980
5410
155981

CONTOH KELUARAN
1

ket : yang tidak valid adalah 5410
'''

n = int(input())
a = 0
nilaisalah = 0
while a != n :
    a += 1
    data = str(input())
    if str((len(data)-1) %2) != data[-1]:
        nilaisalah += 1
print(nilaisalah)















