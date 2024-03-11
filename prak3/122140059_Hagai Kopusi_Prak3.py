#Nama   : Hagai Kopusi Sinulingga
#NIM    : 122140059

print("====================================")
print("               SOAL 2               ")             
print("====================================")


class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga

        # Menambahkan data barang ke list_barang
        Dagangan.list_barang.append((self.__nama, self.__stok, self.__harga))
        Dagangan.jumlah_barang += 1

    def hapus_barang(self):
        # Menghapus data barang dari list_barang
        Dagangan.list_barang.remove((self.__nama, self.__stok, self.__harga))
        Dagangan.jumlah_barang -= 1
        print(f"{self.__nama} dihapus dari toko!")

    def lihat_barang():
        print(f"Jumlah barang dagangan pada toko: {Dagangan.jumlah_barang} buah")
        for idx, barang in enumerate(Dagangan.list_barang, start=1):
            nama, stok, harga = barang
            print(f"{idx}. {nama} seharga Rp {harga} (stok: {stok})")

# Contoh penggunaan
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()

# Menghapus instansi Dagangan1
Dagangan1.hapus_barang()
Dagangan.lihat_barang()
