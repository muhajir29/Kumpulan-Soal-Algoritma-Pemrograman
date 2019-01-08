'''
CEK DATA

pak ayyub membacakan sekumpulan data dalam rentang [1000 , 9 999 999 ] melalui telepon. Digit terakhir data menunjukan panjang tiap data.
anda ditugaskan untuk menghitungan banyaknya data yang tidak sesuai panjangnya.
'''
'''
FORMAT MASUKAN 
baris pertama memmuat seuatu bilanagan bilay , n, diikuti n baris yang merupakan data yang dibacakan

FORMAT KELUARAN
sebuah bilangan bulat yang merupakan banyaknya data yang panjang tidak sesuai. Keluaran diakhiri newline
'''
'''
CONTOH MASUKAN
5
5644
3413
27985
5411
155986

CONTOH KELUARAN
2

'''

n = int(input("imam"))
datasalah = 0
for i in range(n):
    data = int(input())
    strdata = str(data)
    if str(len(strdata)) != str(strdata[-1]):
        datasalah += 1
print(datasalah)


