#Achmad Gibran - 202412003

class Burung:
    def terbang(self):
        return "Burung terbang tinggi"

class Pesawat:
    def terbang(self):
        return "Pesawat lepas landas"

# Fungsi yang menerima objek apa pun
def uji_terbang(obj):
    print(obj.terbang())

# Duck typing
b = Burung()
p = Pesawat()

# Memanggil fungsi yang sama dengan objek berbeda
uji_terbang(b)
uji_terbang(p)