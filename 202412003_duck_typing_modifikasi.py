#Achmad Gibran - 202412003

class Laptop:
    def nyalakan(self):
        return "Laptop menyala: Selamat datang di Windows."

class Smartphone:
    def nyalakan(self):
        return "Smartphone menyala: Logo Android muncul."

# fungsi tes_nyala(obj) yang memanggil method nyalakan().
def tes_nyala(obj):
    # Fungsi hanya peduli objek memiliki method nyalakan(),
    # tidak peduli apa tipe class-nya.
    print(obj.nyalakan())

# Demonstrasi
l = Laptop()
s = Smartphone()

tes_nyala(l)
tes_nyala(s)