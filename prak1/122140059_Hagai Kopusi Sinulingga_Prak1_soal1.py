#Nama   : Hagai Kopusi Sinulingga
#NIM    : 122140059


print("====================================")
print("               CASE 1               ")             
print("====================================")

# Menerima input dari pengguna
b_bawah = int(input("Masukkan batas bawah: "))
b_atas = int(input("Masukkan batas atas: "))

# Memeriksa apakah batas bawah dan atas di bawah nol
if b_bawah < 0 or b_atas < 0:
    print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah Nol")
else:
    total_ganjil = 0

    # Menjumlahkan bilangan ganjil di antara batas bawah dan atas
    print(f"Bilangan ganjil antara {b_bawah} dan {b_atas} dijumlahkan:")
    for bilangan in range(b_bawah, b_atas):
        if bilangan % 2 != 0:
            print(bilangan)
            total_ganjil += bilangan

    # Menampilkan hasil penjumlahan bilangan ganjil
    print(f"Total: {total_ganjil}")