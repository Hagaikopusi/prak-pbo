#Nama   : Hagai Kopusi Sinulingga
#NIM    : 122140059

print("====================================")
print("               SOAL 1               ")             
print("====================================\n")





class Hewan:
    def __init__(self, nama, jenis_kelamin):
        """
        Constructor untuk kelas Hewan.
        
        Args:
            nama (str): Nama hewan.
            jenis_kelamin (str): Jenis kelamin hewan.
        """
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
    
    def bersuara(self):
        """
        Metode untuk membuat hewan bersuara.
        (Diimplementasikan di kelas anak)
        """
        pass
    
    def makan(self):
        """Metode untuk membuat hewan makan."""
        print(f"{self.nama} sedang makan: tulang")
    
    def minum(self):
        """Metode untuk membuat hewan minum."""
        print(f"{self.nama} sedang minum: air")


class Kucing(Hewan):
    def bersuara(self):
        """
        Implementasi metode bersuara khusus untuk kucing.
        """
        print(f"Kucing {self.nama} bersuara: Meong!")


class Anjing(Hewan):
    def bersuara(self):
        """
        Implementasi metode bersuara khusus untuk anjing.
        """
        print(f"Anjing {self.nama} bersuara: Guk Guk!")


# Contoh penggunaan
hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")

print(hewan1.nama)  # Output: Kiki
print(hewan2.nama)  # Output: Ichi

hewan1.bersuara()   # Output: Kucing Kiki bersuara: Meong!
hewan1.makan()      # Output: Kucing Kiki sedang makan: tulang

hewan2.bersuara()   # Output: Anjing Ichi bersuara: Guk Guk!
hewan2.makan()      # Output: Anjing Ichi sedang makan: tulang
