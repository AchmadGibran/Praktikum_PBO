# Nama: Achmad Gibran - NIM: 202412003 

class Mahasiswa:
    def __init__(self, nim, nama, semester=1, ipk=0.0):
        self.nim = nim      
        self.nama = nama    
        self._semester = semester 
        self.__ipk = ipk    

    # Getter untuk IPK Private
    def get_ipk(self):
        return self.__ipk

    # Setter untuk IPK Private
    def set_ipk(self, nilai_baru):
        if not (0.0 <= nilai_baru <= 4.0):
            raise ValueError("IPK harus antara 0.0 dan 4.0.")
        self.__ipk = nilai_baru

    # Getter untuk Semester Protected
    def get_semester(self):
        return self._semester

    # Setter untuk Semester Protected
    def set_semester(self, nilai_baru):
        if nilai_baru < 1:
            raise ValueError("Semester harus minimal 1.")
        self._semester = nilai_baru

# PENGGUNAAN (Membuat 2 objek Mahasiswa)
if __name__ == "__main__":
    
    print("--- PENGUJIAN 2 OBJEK MAHASISWA ---")
    
    mhs1 = Mahasiswa("202412003", "Gibran", semester=3, ipk=3.86)
    mhs2 = Mahasiswa("202412002", "Bramantio", semester=3, ipk=3.80)
    
    print("\n-- Data Mahasiswa 1 --")
    print(f"NIM: {mhs1.nim}")
    print(f"Nama: {mhs1.nama}")
    print(f"Semester: {mhs1.get_semester()}")
    print(f"IPK: {mhs1.get_ipk()}")
    
    print("\n-- Data Mahasiswa 2 --")
    print(f"NIM: {mhs2.nim}")
    print(f"Nama: {mhs2.nama}")
    print(f"Semester: {mhs2.get_semester()}")
    print(f"IPK: {mhs2.get_ipk()}")