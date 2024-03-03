#Nama   : Hagai Kopusi Sinulingga
#NIM    : 122140059

print("====================================")
print("               CASE 2               ")             
print("====================================")

import time

# Decorator untuk mencatat waktu eksekusi method
def catat_waktu_eksekusi(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        waktu_eksekusi = end_time - start_time
        print(f"Method {func.__name__} dieksekusi dalam {waktu_eksekusi:.4f} detik.")
        return result
    return wrapper

class PemainMinecraft:
    # Constructor
    def __init__(self, nama):
        self.nama = nama
        self.kesehatan = 100
        self.posisi = (0, 0, 0)
        print(f"Pemain {self.nama} muncul dengan kesehatan {self.kesehatan} di posisi {self.posisi}.")

    # Decorator diterapkan pada method mine_block
    @catat_waktu_eksekusi
    def gali_blok(self, jenis_blok):
        print(f"{self.nama} sedang menggali blok {jenis_blok}.")
        self.kesehatan -= 10
        print(f"{self.nama} kehilangan 10 kesehatan. Kesehatan: {self.kesehatan}")

    # Decorator diterapkan pada method build_block
    @catat_waktu_eksekusi
    def bangun_blok(self, jenis_blok):
        print(f"{self.nama} sedang membangun blok {jenis_blok}.")
        self.kesehatan -= 5
        print(f"{self.nama} kehilangan 5 kesehatan. Kesehatan: {self.kesehatan}")

    # Destructor
    def __del__(self):
        print(f"Pemain {self.nama} meninggalkan permainan dengan kesehatan {self.kesehatan}.")

# Penggunaan class dan method
pemain1 = PemainMinecraft("Steve")
pemain1.gali_blok("Batu")
pemain1.bangun_blok("Kayu")

pemain2 = PemainMinecraft("Alex")
pemain2.gali_blok("Tanah")
