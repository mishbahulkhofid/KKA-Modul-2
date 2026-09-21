"""
Latihan 3: Data Loading & Inspection
Modul KKA-Modul-2 - EDA dengan NumPy & Pandas

Tujuan:
- Melakukan Data Loading dan Data Inspection terhadap sebuah dataset.
"""

import pandas as pd
from pathlib import Path

print("=== Latihan 3: Data Loading & Inspection ===")

# Path CSV di folder yang sama dengan file ini agar bisa dijalankan dari mana saja
csv_path = Path(__file__).parent / "data_kantin.csv"
print(f"Membaca file: {csv_path}")

df = pd.read_csv(csv_path)

print("\n--- 5 baris pertama (head) ---")
print(df.head())

print("\n--- Tipe data & jumlah non-null tiap kolom (info) ---")
print(df.info())

print("\n--- Statistik ringkas kolom numerik (describe) ---")
print(df.describe())

print("\n--- Jumlah (baris, kolom) (shape) ---")
print(df.shape)

print("\n--- Jumlah data kosong tiap kolom (tambahan untuk analisis) ---")
print(df.isnull().sum())

print("\n=== Tugas Analisis 3 ===")
print("""
Jawaban (berdasarkan df.info() pada data_kantin.csv):
- Total baris dataset: 110 baris.
- Kolom 'menu'    : hanya 107 non-null (kurang 3 dari total) -> ada 3 menu kosong.
- Kolom 'terjual' : hanya 104 non-null (kurang 6 dari total) -> ada 6 terjual kosong.
- Kolom 'tanggal', 'kategori', 'harga': 110 non-null (lengkap, tidak ada yang hilang).

Artinya:
- Angka non-null yang lebih sedikit dari jumlah baris total = ada missing
  value (data hilang) pada kolom tersebut.
- Pada kasus ini 'menu' kehilangan 3 data dan 'terjual' kehilangan 6 data.
- Dampaknya: df.describe() otomatis hanya menghitung 104 data pada kolom
  'terjual', dan kolom 'terjual' berubah tipe menjadi float64 (bukan int)
  karena NaN hanya bisa ditampung tipe float.
- Tindak lanjut: kolom-kolom inilah yang harus dibersihkan pada Latihan 4
  (fillna / dropna) sebelum dianalisis lebih jauh.
""")
