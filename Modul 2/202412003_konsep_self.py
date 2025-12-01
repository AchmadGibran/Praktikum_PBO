class MataKuliah:

    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)

class Mahasiswa:

    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

# Membuat 2 mata kuliah
mk_dasar = MataKuliah("TI101", "Pemrograman Dasar")
mk_pbo = MataKuliah("TI102", "Pemrograman Berorientasi Objek")

# Membuat 3 mahasiswa
m1 = Mahasiswa("202412003", "Achmad Gibran")
m2 = Mahasiswa("202412002", "Bramantio")
m3 = Mahasiswa("202412001", "Firman")

# Mendaftarkan mahasiswa ke masing-masing mata kuliah

mk_dasar.tambah_mahasiswa(m1)
mk_dasar.tambah_mahasiswa(m2)

mk_pbo.tambah_mahasiswa(m1)
mk_pbo.tambah_mahasiswa(m2)
mk_pbo.tambah_mahasiswa(m3)

print("Mata Kuliah:", mk_dasar.nama)
print(mk_dasar.daftar_mahasiswa())
print("Jumlah:", mk_dasar.jumlah_mahasiswa())

print("\nMata Kuliah:", mk_pbo.nama)
print(mk_pbo.daftar_mahasiswa())
print("Jumlah:", mk_pbo.jumlah_mahasiswa())