print("=============================")
print("Operasi Matematika")
print("1. Tambah    [+]")
print("2. Kurang    [-]")
print("3. Kali      [*]")
print("4. Bagi      [/]")
print("=============================")
i=int(input("Pilih Operasi (1/2/3/4): "))
print("=============================")
n=int(input("Masukkan Bilangan Pertama: "))
g=int(input("Masukkan Bilangan Kedua: "))

def jmlh(n,g):
    j = n+g
    return j
def krng(n,g):
    k = n-g
    return k
def kli(n,g):
    kl=n*g
    return kl
def bgi(n,g):
    b = n/g
    return b


if i == 1:
    print("Hasil Operasi dari: ",n,"+",g,"=", jmlh(n,g))
elif i == 2:
    print("Hasil Operasi dari: ",n,"-",g,"=", krng(n,g))
elif i == 3:
    print("Hasil Operasi dari: ",n,"*",g,"=", kli(n,g))
else:
    print("Hasil Operasi dari: ",n,"/",g,"=", bgi(n,g))
