# Achmad Gibran - 202412003 

class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)
        
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0.0
        total_skor = sum(nilai.skor for nilai in self.daftar_nilai)
        return total_skor / len(self.daftar_nilai)

class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama

class ProgramStudi:
    def __init__(self, nama, ketua): 
        self.nama = nama
        self.daftar_matakuliah = []

    def tambah_matakuliah(self, mk):
        self.daftar_matakuliah.append(mk)

class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []
    
    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi, nama_prodi)
        self.programs.append(prodi)
        return prodi

def report_program(prodi: ProgramStudi, semua_mahasiswa: list['Mahasiswa']):
    print(f"Program Studi: {prodi.nama}")
    
    matakuliah_codes = [mk.kode for mk in prodi.daftar_matakuliah]
    print("Daftar Matakuliah:", ", ".join(matakuliah_codes) or "-")
    
    print("\nMahasiswa dan rata-rata nilai:")
    for m in semua_mahasiswa:
        relevan = [n for n in m.daftar_nilai if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
        
        if relevan:
            avg = sum(n.skor for n in relevan) / len(relevan)
            print(f"  {m.nim} - {m.nama}: {round(avg, 2)}")
        else:
            print(f"  {m.nim} - {m.nama}: (Tidak ada nilai relevan)")


if __name__ == "__main__":
    uni = Universitas("Universitas A")
    
    # 1. Program Studi
    prodi_ti = uni.buat_program("Teknik Informatika")
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_ak = uni.buat_program("Akuntansi")
    
    # Mata Kuliah untuk Program Studi
    mk_ti_1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk_ti_2 = MataKuliah("TI102", "Struktur Data")
    prodi_ti.tambah_matakuliah(mk_ti_1)
    prodi_ti.tambah_matakuliah(mk_ti_2)
    
    mk_si_1 = MataKuliah("SI201", "Analisis Sistem Informasi")
    mk_si_2 = MataKuliah("SI202", "Basis Data")
    prodi_si.tambah_matakuliah(mk_si_1)
    prodi_si.tambah_matakuliah(mk_si_2)
    
    mk_ak_1 = MataKuliah("AK301", "Pengantar Akuntansi")
    mk_ak_2 = MataKuliah("AK302", "Akuntansi Biaya")
    prodi_ak.tambah_matakuliah(mk_ak_1)
    prodi_ak.tambah_matakuliah(mk_ak_2)
    
    
    # Buat 3 objek Mahasiswa
    m1 = Mahasiswa("202412003", "Gibran")
    m2 = Mahasiswa("202412002", "Bramantio")
    m3 = Mahasiswa("202412001", "Cindy") 
    
    # Tambahkan objek Nilai ke Mahasiswa (menggunakan tambah_nilai())
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))
    m2.tambah_nilai(Nilai("TI101", 90))
    m2.tambah_nilai(Nilai("SI201", 88))
    m3.tambah_nilai(Nilai("SI202", 92))
    m3.tambah_nilai(Nilai("AK301", 75))
    m3.tambah_nilai(Nilai("AK302", 80))

    
    semua_mahasiswa = [m1, m2, m3]

    # DAFTAR MATA KULIAH SETIAP PROGRAM STUDI
    print("\nDAFTAR MATA KULIAH SETIAP PROGRAM STUDI")
    
    def display_matakuliah(prodi: ProgramStudi):
        print(f"Program Studi: {prodi.nama}")
        if not prodi.daftar_matakuliah:
            print("  - Tidak ada mata kuliah.")
            return
        for mk in prodi.daftar_matakuliah:
            print(f"  - {mk.kode}: {mk.nama}")
        print("-" * 20)

    display_matakuliah(prodi_ti)
    display_matakuliah(prodi_si)
    display_matakuliah(prodi_ak)


    # DAFTAR NILAI SETIAP MAHASISWA
    print("\nDAFTAR NILAI SETIAP MAHASISWA")
    
    def display_nilai_mahasiswa(mhs: Mahasiswa):
        print(f"Mahasiswa: {mhs.nim} - {mhs.nama}")
        if not mhs.daftar_nilai:
            print("  - Belum ada nilai.")
            return
        for nilai in mhs.daftar_nilai:
            print(f"  - {nilai.kode_mk}: {nilai.skor}")
        print("-" * 20)
        
    for mhs in semua_mahasiswa:
        display_nilai_mahasiswa(mhs)

    # RATA-RATA NILAI KESELURUHAN MAHASISWA
    print("\nRATA-RATA NILAI KESELURUHAN MAHASISWA")
    for mhs in semua_mahasiswa:
        rata = mhs.rata_rata()
        print(f"  {mhs.nim} - {mhs.nama}: {round(rata, 2)}")
    print("-" * 20)

    # LAPORAN NILAI PER PROGRAM STUDI
    
    report_program(prodi_ti, semua_mahasiswa)
    print("\n")
    report_program(prodi_si, semua_mahasiswa)
    print("\n")
    report_program(prodi_ak, semua_mahasiswa)