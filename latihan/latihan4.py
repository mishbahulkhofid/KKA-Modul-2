"""
Latihan 4: Menangani Missing Value
Modul KKA-Modul-2 - EDA dengan NumPy & Pandas

Tujuan:
- Melakukan Data Cleaning: menangani missing value.
"""

import pandas as pd
from pathlib import Path

print("=== Latihan 4: Menangani Missing Value ===")

csv_path = Path(__file__).parent / "data_kantin.csv"
df = pd.read_csv(csv_path)

print(f"Shape awal: {df.shape}")
print("\n--- Jumlah data kosong tiap kolom (SEBELUM) ---")
print(df.isnull().sum())

# 1. Isi kekosongan kolom 'terjual' dengan 0
#    (angka masih bisa diberi nilai default wajar)
df["terjual"] = df["terjual"].fillna(0)

# 2. Hapus baris jika kolom 'menu' kosong
#    (identitas produk tidak bisa dikarang)
df = df.dropna(subset=["menu"])

# Pastikan 'terjual' kembali ke integer setelah fillna
df["terjual"] = df["terjual"].astype(int)

print("\n--- Jumlah data kosong tiap kolom (SESUDAH) ---")
print(df.isnull().sum())
print(f"\nShape sesudah cleaning: {df.shape}")
print("\n--- 5 baris pertama setelah cleaning ---")
print(df.head())

print("\n=== Tugas Analisis 4 ===")
print("""
Jawaban: Mengapa 'terjual' diisi (fillna) sedangkan 'menu' dihapus (dropna)?

1. Kolom 'terjual' (numerik) -> fillna(0):
   - 'terjual' adalah angka jumlah porsi. Jika kosong, masih masuk akal
     diberi nilai default 0 (dianggap belum ada penjualan tercatat)
     sehingga barisnya tetap bisa dipakai untuk analisis lain
     (tanggal, kategori, harga tetap valid).
   - Jika barisnya langsung dibuang, kita kehilangan informasi tanggal
     dan produk hanya karena satu angka hilang.
   - Pada dataset ini 6 dari 110 baris (~5,5%) kehilangan 'terjual',
     jadi mengisi lebih hemat daripada membuang.

2. Kolom 'menu' (identitas/kunci) -> dropna:
   - 'menu' adalah nama produk, yaitu identitas baris. Jika namanya
     kosong, kita tidak tahu baris itu milik produk apa (Nasi Goreng?
     Es Teh? produk baru?).
   - Mengisi menu kosong dengan tebakan (misal "Unknown") berisiko
     menciptakan produk fiktif yang merusak groupby per menu.
   - Pada dataset ini hanya 3 dari 110 baris (~2,7%) yang kehilangan
     'menu', jadi menghapusnya aman dan tidak banyak mengurangi data.
   - Hasil pada data ini: 110 -> 107 baris setelah dropna(subset=['menu']).

3. Prinsip umumnya:
   - Data numerik yang hilang dan masih bisa diberi nilai netral
     (0, rata-rata, median) -> fillna.
   - Data identitas/kategori kunci yang hilang dan tidak bisa ditebak
     -> dropna, karena menebak identitas = memalsukan data.
""")
