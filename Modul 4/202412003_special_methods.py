#Achmad Gibran - 202412003

class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        # Menggantikan representasi string saat objek diprint
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        # Mengizinkan perbandingan '>': a > b
        return self.nilai > other.nilai

    def __add__(self, other):
        # Mengizinkan operasi penjumlahan '+': a + b
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        # Mengizinkan operasi perkalian '*': b * 2
        return self.nilai * faktor

# Contoh
a = Mahasiswa("Dinda", 95)
b = Mahasiswa("Gibran", 90)

print(a)
print(b)

if b > a:
    print(f"({b.nama} memiliki nilai lebih tinggi)")

print("Total nilai:", a + b)
print("Nilai Gibran x 2 =", b * 2)