#Nama   : Hagai Kopusi Sinulingga
#NIM    : 122140059

print("====================================")
print("               CASE 1               ")             
print("====================================")


class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def method_satu(self):
        # Operasi pada method pertama
        return f"Method Satu: {self.__nama} - {self.__nim}"

    def method_dua(self, parameter):
        # Operasi pada method kedua
        return f"Method Dua dengan parameter: {parameter}"

    def method_tiga(self):
        # Operasi pada method ketiga
        return f"Method Tiga: Angkatan {self.angkatan}, Status Mahasiswa: {self.isMahasiswa}"


# Inisiasi objek pertama dengan nilai isMahasiswa secara eksplisit
mahasiswa1 = Mahasiswa(nim="122140059", nama="Hagai Kopusi", angkatan=2022, isMahasiswa=True)

# Inisiasi objek kedua tanpa menyertakan parameter isMahasiswa (menggunakan default value)
mahasiswa2 = Mahasiswa(nim="122140069", nama="Dono Mahabarata", angkatan=2024)

# Menggunakan setter untuk mengganti nilai nim dan nama
mahasiswa1.set_nim("122140022")
mahasiswa1.set_nama("John Saina")


# Menggunakan getter untuk mendapatkan nilai nim dan nama
print(f"NIM Mahasiswa 1: {mahasiswa1.get_nim()}")
print(f"Nama Mahasiswa 1: {mahasiswa1.get_nama()}")
print(f"NIM Mahasiswa 2: {mahasiswa2.get_nim()}")
print(f"Nama Mahasiswa 2: {mahasiswa2.get_nama()}")

# Memanggil dan menampilkan hasil dari masing-masing method
print(mahasiswa1.method_satu())
print(mahasiswa2.method_dua("Contoh Parameter"))
print(mahasiswa1.method_tiga())
