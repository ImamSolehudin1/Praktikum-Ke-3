print("Menapilkan Bilangan Terbesar dari 7 Data yang di Inputkan")
print("="*50)
A=int(input("Masukan bilangan : "))
B=int(input("Masukan bilangan : "))
C=int(input("Masukan bilangan : "))
D=int(input("Masukan bilangan : "))
E=int(input("Masukan bilangan : "))
F=int(input("Masukan bilangan : "))
G=int(input("Masukan bilangan : "))

maks = 0
if A > B : 
    maks = A
else:
    maks = B

if C > maks :
    maks = C
if D > maks :
    maks = D
if E > maks :
    maks = E
if F > maks :
    maks = F
if G > maks :    
    maks = G
print("Bilangan terbesar",maks)
