'''
PARKIR

suatu gedung memiliki lahan parkir berbayar. pengguna jasa parkir membayar uang parkir berdasarkan lama pemakaian lahan parkir.
biaya parkir untuk bus, mobil dan motor berbeda.
untuk 1 jam pertama biaya yang dikenakan untuk bus sebesar Rp. 5000,
mobil sebesar Rp.3000,sedangkan
untuk motor Rp.2000.
untuk jam berikutnya biaya parkir untuk bus bertambah Rp.3000/jam,
Mobil bertambah sebesar 1500/jam, sedangkan untuk
motor bertambah sebesar 1000 / jam.
jika telah mencapai waktu pemakain selama 14 jam atau lebih maka perhitungan biaya parkir dihentikan.
untuk memudahkan proses perhitungan, maka jumlah jam tidak ada pecahan

'''
'''
FORMAT MASUKAN
masukan berupa tiga bilangan yang terdiri atas jenis kendaraan, dan jam masuk dan jam keluar.
jenis kendaraan 1 menunjukan untuk bus, 2 untuk mobil , dan 3 untuk motor . 
penulisan jam dalam rentang 0 - 24 jam. asumsikan bahwa pemakaian lahan parkir tidak lebih dari 1 hari

FORMAT KELUARAN
keluaran merupakan jumlah uang yang harus dibayarkan pengguna jasa parkir tersebut. baris diakhir newline
'''
'''
CONTOH MASUKAN
1 11 13

CONTOH KELUARAN 
8000
'''

jenis, awal, akhir = map(int, input().split())
jam = (akhir - awal)
awalbus = 5000
awalmobil = 3000
awalmotor = 2000

biaya = 0

if jenis == 1:
    if jam <= 1:
        biaya = awalbus
    elif jam >= 14:
        biaya = awalbus + (13*3000)
    else:
        biaya = awalbus + ((jam-1)*3000)
elif jenis == 2:
    if jam <= 1:
        biaya = awalmobil
    elif jam >= 14:
        biaya = awalmobil + (13*1500)
    else:
        biaya = awalmobil + ((jam-1)*1500)
elif jenis == 3:
    if jam <= 1:
        biaya = awalmotor
    elif jam >= 14:
        biaya = awalmotor + (13*1000)
    else:
        biaya = awalmotor + ((jam-1)*1000)

print(biaya)

