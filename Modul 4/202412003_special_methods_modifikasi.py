#Achmad Gibran - 202412003

class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        # Representasi string
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    # Implementasi __len__
    def __len__(self):
        # Mengembalikan panjang nama mahasiswa
        return len(self.nama)

    # Implementasi __eq__
    def __eq__(self, other):
        # Dua mahasiswa sama jika nilai mereka sama
        return self.nilai == other.nilai

    # Metode yang sudah ada (untuk operasi matematika)
    def __gt__(self, other):
        return self.nilai > other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor


# membuat minimal 2 objek Mahasiswa
m1 = Mahasiswa("Dinda", 95)
m2 = Mahasiswa("Gibran", 90)
m3 = Mahasiswa("Achmad", 80) # Objek tambahan untuk demonstrasi __eq__ dan sorted

print("--- Data Mahasiswa dan Representasi String ---")
# Representasi string (print(obj))
print(m1)
print(m2)
print(m3)

print("\n--- Implementasi __len__ ---")
print(f"Panjang nama {m1.nama}: {len(m1)}")
print(f"Panjang nama {m2.nama}: {len(m2)}")

print("\n--- Perbandingan Kesetaraan (Menggunakan ==) ---")
print(f"Apakah nilai {m1.nama} ({m1.nilai}) sama dengan {m2.nama} ({m2.nilai})? {m1 == m2}")
print(f"Apakah nilai {m1.nama} ({m1.nilai}) sama dengan {m3.nama} ({m3.nilai})? {m1 == m3}")

print("\n--- Operasi Matematika ---")
print(f"Total nilai {m1.nama} dan {m2.nama}: {m1 + m2}")
print(f"Nilai {m2.nama} dikali 2: {m2 * 2}")

print("\n--- Pengurutan (Menggunakan sorted dan lambda) ---")
list_mahasiswa = [m1, m2, m3]
list_terurut = sorted(list_mahasiswa, key=lambda x: x.nilai)

print("List Mahasiswa Terurut berdasarkan Nilai:")
for m in list_terurut:
    print(m)