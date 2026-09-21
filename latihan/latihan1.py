"""
Latihan 1: Operasi Dasar NumPy Array
Modul KKA-Modul-2 - EDA dengan NumPy & Pandas

Tujuan:
- Memahami dan menggunakan library NumPy untuk operasi array dasar.
"""

import numpy as np

print("=== Latihan 1: Operasi Dasar NumPy Array ===")

harga = np.array([5000, 7000, 3000, 12000, 4500])
print("Data harga:", harga)
print("Rata-rata harga:", harga.mean())
print("Harga tertinggi:", harga.max())
print("Harga terendah:", harga.min())
print("Median harga:", np.median(harga))
print("Standar deviasi:", harga.std())
print("Harga setelah diskon 10%:", harga * 0.9)

print("\n=== Perbandingan dengan list Python biasa ===")
harga_list = [5000, 7000, 3000]
print("List:", harga_list)

# List Python * integer = replikasi (pengulangan), bukan operasi matematis
print("List * 2 (integer):", harga_list * 2)

# List Python * float = ERROR
try:
    hasil = harga_list * 0.9
    print("List * 0.9:", hasil)
except TypeError as e:
    print(f"List * 0.9 -> ERROR TypeError: {e}")

# Cara list agar bisa diskon harus pakai looping / list comprehension
harga_diskon_list = [h * 0.9 for h in harga_list]
print("List dengan list comprehension:", harga_diskon_list)

# Cara NumPy: langsung vektorisasi tanpa loop
harga_np = np.array(harga_list)
print("NumPy array * 0.9:", harga_np * 0.9)

print("\n=== Tugas Analisis 1 ===")
print("""
Jawaban:
1. [5000, 7000, 3000] * 0.9 menghasilkan ERROR:
   TypeError: can't multiply sequence by non-int of type 'float'.
   Penyebabnya: operator * pada list Python hanya mendukung pengali
   integer dan artinya REPIKASI (misal [1,2] * 2 = [1,2,1,2]),
   bukan perkalian matematis per elemen.

2. Sedangkan pada NumPy array, harga * 0.9 berjalan langsung ke
   seluruh elemen sekaligus (disebut operasi vectorized).
   Hasilnya: array([4500., 6300., 2700.]) -> tiap harga otomatis
   didiskon 10% tanpa perlu loop.

3. Mengapa berbeda?
   - List Python adalah koleksi objek umum yang fleksibel (bisa campur
     string, int, dll), jadi Python tidak tahu harus mengartikan * 0.9
     sebagai apa.
   - NumPy array adalah blok angka homogen (satu tipe data, misal int64)
     yang disimpan rapat di memori, sehingga NumPy bisa menerapkan
     operasi matematis ke semua elemen sekaligus dalam bahasa C yang
     cepat.

4. Analogi modul: list seperti menghitung diskon satu-satu pakai
   kalkulator manual (harus looping), NumPy seperti mesin kasir yang
   memproses seluruh struk dalam satu perintah.
""")
