'''
 Create 44.Belajar_memanah.py

Klimatono sedang belajar memanah. Bantulah dia untuk mencatat sasaran yang berhasil dipanahnya.

Format Masukan
Baris pertama berisikan banyaknya sasaran, n. Baris-baris berikutnya ialah daftar sasaran yang berhasil dipanah (dinomori 1 s/d n) 
atau 0 jika tidak ada sasaran yang kena. Akhir latihan Klimantono ditandai dengan suatu huruf.

Format Keluaran
Rangkaian n simbol dengan tanda '-' merupakan sasaran yang tidak kena dan tanda '*' merupakan sasaran yang kena. Baris diakhiri dengan newline.

Petunjuk untuk Python
Gunakan blok try except untuk mendeteksi masukan huruf.

Suatu list, x, dapat diinisialisasi berisikan 5 buah nilai 0 (yaitu [0, 0, 0, 0, 0] ) dengan pernyataan berikut:

x = [0] * 5
Tanpa inisialisasi, kita tidak dapat mengakses indeks di luarnya. Misalnya, dengan inisialisasi di atas, x[i] valid untuk 0 <= i <= 4, 
tetapi akses ke x[5] menghasilkan runtime error karena belum tersedia.
 
Contoh Masukan
10
0
3
7
2
3
0
10
X

Contoh Keluaran
-**---*--*


'''


#COBA KEDUA JENIS JAWABAN
#CODE PERTAMA

# n = int(input())

# target = [0] * (n)

# while True:
#     tembak = input()
#     if tembak.isalpha():
#         break
#     elif tembak == "0":
#         continue
#     else:
#         try:
#             target[int(tembak) - 1] += 1
#         except:
#             continue


# result = ""
# for i in target:
#     if i == 0:
#         result += "-"
#     else:
#         result += "*"
# print(result)

#CODE KE DUA

n = int(input())
sc = ['-'] * n

while True:
    try:
        x = int(input())
        if x == 0:
            pass
        else:
            sc[x - 1] = "*"
    except:
        break
print(''.join(sc))

#THALIA
