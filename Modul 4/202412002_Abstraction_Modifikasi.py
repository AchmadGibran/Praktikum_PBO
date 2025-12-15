#Achmad Gibran - 202412003

from abc import ABC, abstractmethod
import math

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * math.pi * self.jari_jari

# Class Persegi
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi

# Tambahan Parameter Warna pada Class PersegiPanjang
class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar, warna="Tidak Berwarna"):
        self.panjang = panjang
        self.lebar = lebar
        self.warna = warna

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def info(self):
        return (f"Persegi Panjang: P={self.panjang}, L={self.lebar}, "
                f"Warna='{self.warna}'")

# Menampilkan
print("--- contoh implementasi bentuk ---")
l = Lingkaran(5)
p = PersegiPanjang(4, 3, "Merah")
k = Persegi(6)

print(f"Luas Lingkaran: {l.luas():.2f}")
print(f"Keliling Lingkaran: {l.keliling():.2f}")
print(f"Info Objek Persegi Panjang: {p.info()}") 
print(f"Luas Persegi (sisi=6): {k.luas()}")
print(f"Keliling Persegi (sisi=6): {k.keliling()}")