#Nama   : Hagai Kopusi Sinulingga
#NIM    : 122140059


print("====================================")
print("               CASE 2               ")             
print("====================================")

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Memeriksa apakah jari-jari lingkaran tidak boleh negatif
if jari_jari < 0:
    print("Jari-jari lingkaran tidak boleh negatif")
else:
    # Menghitung luas dan keliling lingkaran
    luas = 3.14 * (jari_jari ** 2)
    keliling = 2 * 3.14 * jari_jari

    # Menampilkan hasil
    print(f"Luas : {luas:.2f}")
    print(f"Keliling : {keliling:.2f}")