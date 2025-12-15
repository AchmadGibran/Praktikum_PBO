#Achmad Gibran - 202412003

def operasi():
    print("--- Operasi Matematika Aman ---")
    print("Pilih operasi:")
    print("1. Pembagian")
    print("2. Perkalian")

    pilihan = input("Masukkan pilihan (1/2): ").strip()
    x = input("Masukkan angka pertama: ").strip()
    y = input("Masukkan angka kedua: ").strip()

    try:
        # Validasi 1: input tidak boleh kosong
        if x == "" or y == "":
            raise ValueError("Input tidak boleh kosong")
            
        a = float(x)
        b = float(y)
        
        # Validasi 2: bilangan harus positif
        if a < 0 or b < 0:
            raise ValueError("Hanya angka positif yang diperbolehkan")

        if pilihan == "1":
            # Pembagian (dapat memunculkan ZeroDivisionError jika b=0)
            hasil = a / b
        elif pilihan == "2":
            # Perkalian
            hasil = a * b
        else:
            raise ValueError("Pilihan operasi tidak valid. Gunakan 1 atau 2.")

    except ValueError as ve:
        # Menangkap error yang dibuat secara manual (ValueError)
        # dan error konversi tipe data
        print(f"Input salah: {ve}")
    except ZeroDivisionError:
        # Menangkap error pembagian dengan nol
        print("Penyebut tidak boleh nol pada operasi pembagian!")
    except Exception as e:
        # Menangkap semua error lain yang tidak terduga
        print(f"Terjadi kesalahan: {e}")
    else:
        # Blok ini dieksekusi HANYA jika TIDAK ADA error di blok try
        print(f"Hasil operasi: {hasil}")
    finally:
        # Blok ini SELALU dieksekusi, baik ada error maupun tidak
        print("Selesai memproses input.")

if __name__ == "__main__":
    operasi()