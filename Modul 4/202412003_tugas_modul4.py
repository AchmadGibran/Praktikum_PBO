#Achmad Gibran - 202412003

from abc import ABC, abstractmethod

# Class Abstrak: Pengguna
class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama
    
    @abstractmethod
    def akses(self):
        # Method abstrak yang harus diimplementasikan oleh turunan
        pass

# Class Turunan: Member
class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin
        
    # Implementasi method abstrak dari Pengguna
    def akses(self):
        return f"Member {self.nama} memiliki hak akses penuh."

#  SPECIAL METHODS

    # __str__ (Info Member)
    def __str__(self):
        # Menampilkan "Member: Nama - Poin: X"
        return f"Member: Nama={self.nama} - Poin:{self.poin}"
    
    # __add__ (Menjumlahkan poin dua member)
    def __add__(self, other):
        return self.poin + other.poin
        
    # __len__ (Mengembalikan panjang nama)
    def __len__(self):
        return len(self.nama)

# CUSTOM EXCEPTION

class PoinTidakValidError(Exception):
    """Exception untuk poin yang nilainya negatif."""
    pass

# --- FUNGSI UTAMA ---
def buat_member():
    valid_input = False
    
    while not valid_input:
        nama = input("Masukkan Nama Member: ").strip()
        poin_str = input("Masukkan Poin: ").strip()
        
        try:
            # Exception Handling: Input kosong
            if not poin_str:
                raise ValueError("Input poin tidak boleh kosong.")

            poin = int(poin_str)

            # Custom Exception: Poin negatif
            if poin < 0:
                raise PoinTidakValidError("Poin harus angka positif (minimal 0).")
            
        except ValueError as e:
            # Tangani jika input bukan angka atau kosong
            print(f"ERROR: {e}. Harap masukkan bilangan bulat.")
            continue
            
        except PoinTidakValidError as e:
            # Tangani custom exception untuk poin negatif
            print(f"ERROR: {e}")
            continue
            
        else:
            valid_input = True
            return Member(nama, poin)

if __name__ == "__main__":
    print("--- PROGRAM MEMBER ---")
    
    # Buat 2 objek Member
    member1 = buat_member()
    member2 = buat_member()

    print("\n===============================")
    print("HASIL PENGUJIAN OOP:")
    print("===============================")
    
    # Info Member (print())
    print(f"Info Member 1: {member1}")
    print(f"Info Member 2: {member2}")
    
    # Implementasi Abstraksi
    print(f"Hak Akses Member 1: {member1.akses()}")
    
    # Jumlah poin (m1 + m2)
    print(f"Jumlah Poin (m1 + m2): {member1 + member2}")
    
    # Panjang nama (len(m1))
    print(f"Panjang Nama {member1.nama}: {len(member1)}")
    
    # Uji Exception (Poin negatif) - Sudah diuji dalam fungsi buat_member()
    print("Uji Exception Poin Negatif: Telah diuji di awal input.")