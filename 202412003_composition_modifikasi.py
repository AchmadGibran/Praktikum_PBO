#Achmad Gibran - 202412003

class Penulis:
    def __init__(self, nama):
        self.nama = nama
    
    def get_nama(self):
        return self.nama

# Class Buku yang memiliki Penulis (composition)
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        # Komposisi: Buku 'memiliki' objek Penulis
        self.penulis = penulis 

    def info_buku(self):
        # Akses data penulis melalui objek Penulis yang dimiliki Buku
        return (f"Judul: {self.judul}\n"
                f"Ditulis oleh: {self.penulis.get_nama()}")

# Demonstrasi

# Instansiasi objek Penulis
penulis_novel = Penulis("Andrea Hirata")

# Instansiasi objek Buku, dengan memasukkan objek Penulis (Komposisi)
buku_laskar_pelangi = Buku("Laskar Pelangi", penulis_novel)

# Akses dan cetak data
print(buku_laskar_pelangi.info_buku())

# Akses data penulis secara langsung dari objek buku
print(f"Nama Penulis (diakses langsung): {buku_laskar_pelangi.penulis.nama}")