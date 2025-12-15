#Achmad Gibran - 202412003

import math

#Class Parent: Karyawan
class Karyawan:
    #Class dasar untuk semua karyawan.
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        #Menampilkan gaji pokok.#
        return f"{self.nama} (Karyawan): Gaji Pokok = Rp{self.gaji_pokok:,.0f}"

#Child Class: Manager (inherits Karyawan)
class Manager(Karyawan):
    #Class turunan yang merepresentasikan Manajer.
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def info_gaji(self):
        #Override: Menampilkan gaji total (pokok + tunjangan).#
        gaji_total = self.gaji_pokok + self.tunjangan
        return f"{self.nama} (Manager): Gaji Total = Rp{gaji_total:,.0f} (Pokok + Tunjangan)"

#Child Class: Programmer (inherits Karyawan)
class Programmer(Karyawan):
    #Class turunan yang merepresentasikan Programmer.#
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    def info_gaji(self):
        #Override: Menampilkan gaji total (pokok + bonus).#
        gaji_total = self.gaji_pokok + self.bonus
        return f"{self.nama} (Programmer): Gaji Total = Rp{gaji_total:,.0f} (Pokok + Bonus)"

#Composition: Class Departemen
class Departemen:
    #Class yang menggunakan Komposisi (memiliki daftar karyawan).#
    def __init__(self, nama):
        self.nama = nama
        # Komposisi: Memiliki daftar objek Karyawan
        self.daftar_karyawan = [] 

    def tambah_karyawan(self, karyawan):
        #Menambahkan objek Karyawan ke daftar.#
        self.daftar_karyawan.append(karyawan)

    def tampilkan_karyawan(self):
        #Menampilkan info gaji semua karyawan (Polimorfisme dalam aksi).#
        print(f"\n===== Info Gaji Departemen {self.nama} =====")
        for karyawan in self.daftar_karyawan:
            # Polimorfisme: Memanggil info_gaji() yang berbeda tergantung tipe objek
            print(karyawan.info_gaji())
        print("=======================================")


# Instansiasi objek karyawan
manager1 = Manager("Ali", 8000000, 2000000)
manager2 = Manager("Bima", 9000000, 2500000)
programmer1 = Programmer("Cinta", 6000000, 1500000)
programmer2 = Programmer("Dina", 7500000, 1800000)

# Instansiasi objek Departemen
dept_it = Departemen("Teknologi Informasi")

# Tambahkan karyawan ke departemen
dept_it.tambah_karyawan(manager1)
dept_it.tambah_karyawan(manager2)
dept_it.tambah_karyawan(programmer1)
dept_it.tambah_karyawan(programmer2)

# Tampilkan info gaji semua karyawan
dept_it.tampilkan_karyawan()