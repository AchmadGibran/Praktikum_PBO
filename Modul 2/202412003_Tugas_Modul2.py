#Achmad Gibran - 202412003

from datetime import date

# CLASS BUKU
class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul
        self.penulis = penulis
        self.kode_buku = kode_buku
        self._stok = stok                    # protected
        self.__lokasi_rak = lokasi_rak       # private

    # Getter & Setter lokasi rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi):
        self.__lokasi_rak = lokasi

    # Tambah stok
    def tambah_stok(self, jumlah=1):
        self._stok += jumlah

    # Kurangi stok
    def kurangi_stok(self, jumlah=1):
        if self._stok >= jumlah:
            self._stok -= jumlah
            return True
        return False

    def info_buku(self):
        return f"{self.kode_buku} - {self.judul} ({self._stok} tersedia)"


# CLASS PEMINJAMAN
class Peminjaman:
    def __init__(self, kode_buku, tanggal_pinjam, tanggal_kembali=None, status="Dipinjam"):
        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    def info_peminjaman(self):
        return f"Kode Buku: {self.kode_buku}, Pinjam: {self.tanggal_pinjam}, Kembali: {self.tanggal_kembali}, Status: {self.status}"


# CLASS ANGGOTA
class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam=3):
        self.id_anggota = id_anggota
        self.nama = nama
        self._maks_pinjam = maks_pinjam        # protected
        self.__status_aktif = True             # private
        self.daftar_peminjaman = []            # aggregation

    # Getter & Setter status anggota
    def get_status(self):
        return self.__status_aktif

    def set_status(self, aktif):
        self.__status_aktif = aktif

    # Pinjam buku
    def pinjam_buku(self, buku: Buku):
        if not self.__status_aktif:
            print("Anggota tidak aktif!")
            return

        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print("Maksimal peminjaman tercapai!")
            return

        if buku.kurangi_stok():
            peminjaman = Peminjaman(
                kode_buku=buku.kode_buku,
                tanggal_pinjam=date.today()
            )
            self.daftar_peminjaman.append(peminjaman)
            print(f"{self.nama} berhasil meminjam {buku.judul}")
        else:
            print("Stok buku habis!")

    # Mengembalikan buku
    def kembalikan_buku(self, buku: Buku):
        for p in self.daftar_peminjaman:
            if p.kode_buku == buku.kode_buku and p.status == "Dipinjam":
                p.status = "Dikembalikan"
                p.tanggal_kembali = date.today()
                buku.tambah_stok()
                print(f"{self.nama} mengembalikan {buku.judul}")
                return
        print("Buku tidak ditemukan dalam daftar peminjaman.")

    def info_anggota(self):
        return f"ID: {self.id_anggota}, Nama: {self.nama}, Status: {self.__status_aktif}"


# DEMONSTRASI PROGRAM

# 1. Buat 3 buku
b1 = Buku("Laskar Pelangi", "Andrea Hirata", "B001", 3, "Rak A1")
b2 = Buku("Bumi", "Tere Liye", "B002", 2, "Rak B2")
b3 = Buku("Filosofi Teras", "Henry Manampiring", "B003", 1, "Rak C3")

# 2. Buat 2 anggota
a1 = Anggota("A01", "Gibran")
a2 = Anggota("A02", "Andi")

# 3. Anggota 1 pinjam 2 buku
a1.pinjam_buku(b1)
a1.pinjam_buku(b2)

# 4. Anggota 2 pinjam 1 buku
a2.pinjam_buku(b3)

# 5. Pengembalian buku
a1.kembalikan_buku(b1)


# OUTPUT
print("\nINFORMASI BUKU")
print(b1.info_buku())
print(b2.info_buku())
print(b3.info_buku())

print("\nINFORMASI ANGGOTA")
print(a1.info_anggota())
print(a2.info_anggota())

print("\nDAFTAR PEMINJAMAN ANGGOTA")
print(f"Peminjaman {a1.nama}:")
for p in a1.daftar_peminjaman:
    print("-", p.info_peminjaman())

print(f"\nPeminjaman {a2.nama}:")
for p in a2.daftar_peminjaman:
    print("-", p.info_peminjaman())
