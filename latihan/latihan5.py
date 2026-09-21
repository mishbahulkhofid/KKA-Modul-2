"""
Latihan 5: Menangani Duplikat dan Tipe Data
Modul KKA-Modul-2 - EDA dengan NumPy & Pandas

Tujuan:
- Melakukan Data Cleaning: menangani duplikat dan tipe data yang tidak sesuai.
"""

import pandas as pd
from pathlib import Path

print("=== Latihan 5: Menangani Duplikat dan Tipe Data ===")

csv_path = Path(__file__).parent / "data_kantin.csv"
df = pd.read_csv(csv_path)

# Ulangi cleaning Latihan 4 agar titik awalnya sama (mandiri, bisa run sendiri)
df["terjual"] = df["terjual"].fillna(0)
df = df.dropna(subset=["menu"])

print(f"Shape setelah Latihan 4 (sebelum drop duplikat): {df.shape}")

# 1. Cek jumlah baris duplikat
jumlah_duplikat = df.duplicated().sum()
print(f"\nJumlah baris duplikat: {jumlah_duplikat}")

# Tampilkan contoh baris duplikat (jika ada)
if jumlah_duplikat > 0:
    print("\nContoh baris duplikat:")
    print(df[df.duplicated(keep=False)].sort_values(by=list(df.columns)).head(10))

# 2. Hapus duplikat
df = df.drop_duplicates()
print(f"\nShape sesudah drop_duplicates(): {df.shape}")

# 3. Memastikan tipe data sudah benar
print("\n--- Tipe data SEBELUM astype ---")
print(df.dtypes)

df["harga"] = df["harga"].astype(int)
df["terjual"] = df["terjual"].astype(int)

print("\n--- Tipe data SESUDAH astype ---")
print(df.dtypes)

print("\n=== Tugas Analisis 5 ===")
print("""
Jawaban (angka sesuai data_kantin.csv 110 baris):
- Setelah Latihan 4: 110 -> 107 baris (3 baris menu kosong dibuang).
- Jumlah duplikat terdeteksi: 5 baris.
- Setelah drop_duplicates(): 107 -> 102 baris.
  Jadi total berkurang 8 baris dari data mentah (3 missing menu + 5 duplikat).

Mengapa penting memastikan tipe data (dtypes) sudah benar?
1. Perhitungan hanya valid bila tipenya numerik. Jika 'harga' terbaca
   sebagai string/object (misal ada "Rp12.000" atau spasi), maka
   harga * terjual akan ERROR atau menghasilkan gabungan string.
2. Kolom 'terjual' awalnya float64 karena ada NaN (NaN hanya bisa hidup
   di float). Setelah fillna(0) harus dikembalikan ke int agar
   merepresentasikan "jumlah porsi" (tidak ada 20.5 porsi) dan hemat memori.
3. Kolom 'tanggal' seharusnya datetime (bukan string) agar bisa diurutkan
   kronologis, difilter per bulan, dan digroupby per hari/minggu.
4. Tipe yang benar membuat describe(), sort_values(), dan groupby()
   berperilaku benar; tipe yang salah membuat angka diurutkan seperti teks
   ("10000" < "2000" secara string) sehingga analisis menyesatkan.
""")
