print("Menampilkan bilangan Terbesar dari 3 buah Bilangan yang diinputkan")
print("="*70)

A=int(input("Masukan Bilangan A : " ))
B=int(input("Masukan Bilangan B : "))
C=int(input("Masukan Bilangan C : "))

maks = 0
if A > B : 
    maks = A
else:
    maks = B

if C > maks :
    maks = C
print("Bilangan Terbesar Adalah : ", maks)
