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
