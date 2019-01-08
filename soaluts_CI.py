'''
DENDA PERPUSTAKAAN

suatu perpustakanaan memiliki 3 level keanggotaan (membership,
yaitu: classic, premier, infinite . jumlah buku yang dapat dipinjam tidak dibatasi .
standar waktu peminjaman buku adalah 5 hari dan berlaku sama untuk seluruh levelkeanggotaan.
perpustakanan ini menerapkan sistem denda jika terjadi keterlambatan pengembalian buku.
cara menghitung lama keterlambatan selalu berpatokan pada standar waktu peminjaman,
misal peminjaman di tanggal 20 dan pengembalian di tanggal 26,
maka lama keterlambatan selama 1 hari .Besaran denda selain dipengaruhi lamanya keterlambatan
juga dipengaruhi level keanggotaan.

untuk classic, jika keterlambatan kurang dari 7 hari dari waktu standar dikenakan denda $4/hari/buku,
jika lebih dari sama dengan 7 hari hari namun kurang dari 14 hari maka akan dikenakan $6/hari/ buku,
jika pengembalian lebih dari dari sama dengan  14 hari maka dikenanakan denda $ 7 /hari/buku.

untuk premier jika keterlambatan kurang dari 7 hari maka dikenakan denda sebesar $3/hari/ buku,
ketrlambatan lebih dari sama dengan 7 hari dikenakn $ 5/hari/ buku .

untuk level infinite berapapun lama keterlambatannya hanya dikenakan denda sebesar $2/hari/ buku>

setiap pengembalian pada tanggal kelitapan 3 mendapat potongan denda sebesar 20 %. perpustakaan tidak ingin kesulitan dalam memberikan
kembaliaan, maka besar denda selalu bilangan bulat dengan pembulatan ke bawah


FORMAT MASUKAN
masukan terdiri dari atas dua baris, baris pertama terdiri atas 2 informasi yang diwakili bilangan bulat mengenai level keanggotaan dan banyaknya buku yang dipinjam.
level keanggotaan 1 untuk level infinite,
2 untuk premier , dan 3 untuk level classic.
baris kedua berisi 2 bilangan bulay yang merupakan informasi tanggal peminjaman dan tanggal pengembalian.
asumsikan bahwa peminjaman dan pengembalian dilakukan di bulan yang sama

FORMAT KELUARAN
keluaran merupakan besaran denda yang harus di bayar oleh pengguna dalam bilangan bulat



CONTOH MASUKAN
3 6
9 30

CONTOH KELUARAN
537

KET: level 3 menenadakan membership level classic .lamanya keterkambatan adalah 16 hari karena seharusnya dikembalikan tanggal 14,
maka besar denda yang dikenakan $7/buku/hari. pengembalian di tanggal 30 mendapat diskon sebesar 20%.

CONTOH MASUKAN
1 10
3 5

CONTOH KELUARAN
0

KET: pengembalian buku masih pada rentang standar

'''

level, buku= map(int, input().split())
awal, akhir = map(int, input().split())
waktu = akhir - awal
keterlambatan = waktu- 5
if waktu <= 5:
    denda= 0
else:
    if level == 1:
        denda = keterlambatan * buku * 2
    if level ==2:
        if keterlambatan < 7:
            denda = keterlambatan * buku * 3
        else:
            denda = (keterlambatan * buku * 5 )
    if level == 3:
        if keterlambatan < 7 :
            denda = keterlambatan * buku * 4
        elif 7 <= keterlambatan < 14:
            denda = keterlambatan * buku * 6
        else:
            denda = keterlambatan * buku * 7
if akhir% 3 == 0:
    diskon = denda*( 20 /100)
    denda = denda - diskon
denda = denda//1
print(int(denda))



















