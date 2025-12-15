#Achmad Gibran - 202412003

class UmurTidakValidError(Exception):
    """Kesalahan umum untuk umur yang tidak masuk akal."""
    pass

class UmurTerlaluMudaError(UmurTidakValidError):
    """Exception jika umur kurang dari 5 tahun."""
    pass

class UmurTerlaluTuaError(UmurTidakValidError):
    """Exception jika umur lebih dari 100 tahun."""
    pass

class AkunTidakDiizinkanError(Exception):
    """Exception jika umur di bawah batas minimum pendaftaran (18 tahun)."""
    pass

# fungsi validasi umur
def set_umur(umur):
    # Validasi Umur Negatif
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    
    # Validasi Umur Terlalu Muda
    if umur < 5:
        raise UmurTerlaluMudaError("Umur minimal adalah 5 tahun.")
        
    # Validasi Umur Maksimum
    if umur > 100:
        raise UmurTerlaluTuaError("Umur maksimum adalah 100 tahun.")
        
    return umur

# fungsi baru
def daftar_akun(umur):
    # Hanya menerima umur 18 ke atas
    if umur < 18:
        raise AkunTidakDiizinkanError(
            f"Umur Anda ({umur} tahun) di bawah batas minimum 18 tahun untuk pendaftaran akun."
        )
    return "Akun berhasil didaftarkan!"


# PROGRAM UTAMA
if __name__ == "__main__":
    umur_valid = False
    
    # Loop untuk meminta input berkali-kali hingga valid
    while not umur_valid:
        try:
            print("\n--- Validasi Umur Registrasi ---")
            u = input("Masukkan umur: ").strip()

            # Mencegah ValueError jika input kosong sebelum konversi
            if not u:
                raise ValueError("Input tidak boleh kosong.")
                
            umur = set_umur(int(u))
            
        except ValueError as e:
            # Menangani input non-angka atau string kosong
            print(f"Error Input: {e}. Harap masukkan bilangan bulat.")
            
        except UmurTerlaluMudaError as e:
            # Menangani umur < 5
            print(f"Error Validasi: {e}")
            
        except UmurTerlaluTuaError as e:
            # Menangani umur > 100
            print(f"Error Validasi: {e}")
            
        except UmurTidakValidError as e:
            # Menangani Umur < 0 
            print(f"Error Validasi: {e}")
            
        else:
            # Jika semua validasi umur (0-100) lolos
            umur_valid = True
            print(f"\n--- Umur ({umur}) Lolos Validasi Awal ---")
            
            # Panggil fungsi pendaftaran akun baru
            try:
                hasil_akun = daftar_akun(umur)
                print(f"Status Akun: {hasil_akun}")
            except AkunTidakDiizinkanError as e:
                print(f"Status Akun: Gagal. {e}")