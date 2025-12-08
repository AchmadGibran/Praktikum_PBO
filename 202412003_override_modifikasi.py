#Achmad Gibran - 202412003

import math

# Class Induk: Bentuk (Menetapkan default 'luas')
class Bentuk:
    def luas(self):
        return 0

# Class Turunan: Persegi (Meng-override 'luas')
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        # Implementasi Persegi
        return self.sisi * self.sisi

# Class Turunan: Lingkaran (Meng-override 'luas')
class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def luas(self):
        # Implementasi lingkaran
        return math.pi * self.radius * self.radius

# Demonstrasi Polimorfisme (Setiap objek memanggil versi 'luas' miliknya sendiri)
persegi_obj = Persegi(4)
lingkaran_obj = Lingkaran(3)

print(persegi_obj.luas())
print(lingkaran_obj.luas())