print("Pemeriksaan Kelipatan 9")
file = int(input("Masukkan angka kelipatan 9 yang ingin diperiksa: "))
def y_9():
    nilai=(file%9)
    return nilai
if y_9()==0:
    print("BENAR")
else:
    print("SALAH")
