"""
Latihan 2: Membuat Series & DataFrame
Modul KKA-Modul-2 - EDA dengan NumPy & Pandas

Tujuan:
- Memahami dan menggunakan library Pandas (Series & DataFrame).
"""

import pandas as pd

print("=== Latihan 2: Membuat Series & DataFrame ===")

# --- Contoh Series (satu kolom) ---
print("\n--- Contoh Series ---")
menu_series = pd.Series(["Nasi Goreng", "Es Teh", "Mie Ayam"])
print(menu_series)
print("Tipe:", type(menu_series))

# --- Contoh DataFrame sesuai modul ---
print("\n--- Contoh DataFrame Kantin ---")
data_kantin = {
    "menu": ["Nasi Goreng", "Es Teh", "Mie Ayam", "Es Teh", None],
    "harga": [12000, 4000, 10000, 4000, 8000],
    "terjual": [23, 40, None, 35, 18],
}
df = pd.DataFrame(data_kantin)
print(df)

print("\n--- Cek data kosong ---")
print(df.isnull().sum())

print("\n--- Info & deskripsi singkat ---")
print(df.info())
print(df.describe(include="all"))

print("\n=== Tugas Analisis 2 ===")
print("""
Jawaban:
1. Kolom yang terlihat memiliki data kosong (None / NaN):
   - Kolom 'menu'     : 1 data kosong (baris ke-5, harga 8000, terjual 18)
   - Kolom 'terjual'  : 1 data kosong (baris ke-3, Mie Ayam harga 10000)
   - Kolom 'harga'    : tidak ada yang kosong.
   (Terbukti dari df.isnull().sum() di atas.)

2. Risiko jika langsung dianalisis tanpa dibersihkan:
   - Perhitungan numerik jadi salah / NaN menular. Contoh:
     total_pendapatan = harga * terjual -> baris Mie Ayam hasilnya NaN,
     lalu sum()/mean() bisa ikut NaN atau mengabaikan data tanpa sadar.
   - Groupby 'menu' akan membuat kelompok NaN tersendiri yang tidak
     bermakna, atau baris tanpa nama menu ikut terhitung sebagai produk.
   - Visualisasi / sorting menempatkan NaN di posisi membingungkan.
   - Keputusan bisnis bisa keliru: misal Mie Ayam terlihat laku 0 padahal
     datanya hilang, atau produk tanpa nama dianggap produk baru.

3. Kesimpulan: data kosong harus ditangani dulu (Latihan 4) sebelum
   analisis — angka yang hilang diisi dengan nilai wajar (fillna) bila
   masih bisa ditebak, sedangkan identitas kunci yang hilang (seperti
   nama menu) lebih aman dihapus (dropna) agar tidak menciptakan
   produk fiktif.
""")
