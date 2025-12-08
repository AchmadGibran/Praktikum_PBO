#Achmad Gibran - 202412003

# Class Person (Superclass)
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    # Method info
    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur} tahun"

# Class Mahasiswa (Subclass) - Mewarisi Person
class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        # super() untuk inisialisasi Parent
        super().__init__(nama, umur)
        self.nim = nim

    # override method info()
    def info(self):
        return f"Mahasiswa: {self.nama}, NIM: {self.nim}, Umur: {self.umur} tahun"

# Instansiasi dan Pemanggilan
orang_biasa = Person("Gibran", 20)
mahasiswa_baru = Mahasiswa("Dinda", 20, "20250813")

print(orang_biasa.info())
print(mahasiswa_baru.info())