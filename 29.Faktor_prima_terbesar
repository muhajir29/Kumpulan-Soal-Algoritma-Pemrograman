def isprime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    return prime
 
 
x = int(input())
HasilBagi = []
for i in range(2,x):
    if x % i == 0:
        HasilBagi.append(i)
 
nilaiprima = []
 
for j in HasilBagi:
    if isprime(j) == True:
        nilaiprima.append(j)
print(max(nilaiprima))
 
 
 
 
