"""
Latihan 6: Data Manipulation (Filtering, Sorting, Groupby)
Modul KKA-Modul-2 - EDA dengan NumPy & Pandas

Tujuan:
- Melakukan Data Manipulation: filtering, sorting, grouping,
  dan membuat kolom turunan.
"""

import pandas as pd
from pathlib import Path

print("=== Latihan 6: Data Manipulation ===")

csv_path = Path(__file__).parent / "data_kantin.csv"
df = pd.read_csv(csv_path)

# --- Cleaning ringkas (gabungan Latihan 4 + 5) agar file mandiri ---
df["terjual"] = df["terjual"].fillna(0)
df = df.dropna(subset=["menu"])
df = df.drop_duplicates()
df["harga"] = df["harga"].astype(int)
df["terjual"] = df["terjual"].astype(int)
print(f"Dataset siap analisis: {df.shape} (baris, kolom)")

# 1. Filtering: hanya menu yang terjual > 20 porsi
laris = df[df["terjual"] > 20]
print("\n--- Filtering: terjual > 20 ---")
print(laris.head())
print(f"Jumlah transaksi laris: {len(laris)} dari {len(df)} transaksi")

# 2. Sorting: urutkan berdasarkan 'terjual' terbanyak
urut = df.sort_values(by="terjual", ascending=False)
print("\n--- Sorting: 5 transaksi paling laris ---")
print(urut[["menu", "harga", "terjual"]].head())

# 3. Kolom turunan: total pendapatan per transaksi
df["total_pendapatan"] = df["harga"] * df["terjual"]
print("\n--- Kolom turunan: total_pendapatan = harga * terjual ---")
print(df[["menu", "harga", "terjual", "total_pendapatan"]].head())

# 4. Agregasi: total pendapatan per menu
ringkasan = df.groupby("menu")["total_pendapatan"].sum().sort_values(ascending=False)
print("\n--- Groupby: total pendapatan per menu (terurut) ---")
print(ringkasan)

terlaris = ringkasan.idxmax()
print(f"\nMenu pendapatan tertinggi: {terlaris} = Rp{ringkasan.max():,}")

print("\n=== Tugas Analisis 6 ===")
print("""
Jawaban (berdasarkan data_kantin.csv setelah dibersihkan, 102 baris):
Hasil groupby total_pendapatan per menu (terurut):
 1. Nasi Goreng : Rp3.924.000
 2. Mie Ayam     : Rp2.410.000
 3. Es Teh       : Rp2.144.000
 4. Es Jeruk     : Rp1.460.000
 5. Roti Bakar   : Rp1.288.000
 6. Kerupuk      : Rp972.000
 7. Teh Hangat   : Rp459.000

Jadi menu dengan total_pendapatan tertinggi adalah NASI GORENG.

Bagaimana informasi ini membantu pengambilan keputusan di kantin?
1. Prioritas stok: bahan baku Nasi Goreng (beras, telur, bumbu, minyak)
   harus selalu aman karena menjadi mesin kas utama. Kekosongan stok
   Nasi Goreng = kehilangan pendapatan terbesar.
2. Strategi menu: Es Teh memang terjual paling banyak per transaksi
   (45 porsi), tetapi harga satuannya kecil sehingga totalnya kalah dari
   Nasi Goreng. Kantin bisa membuat paket bundling "Nasi Goreng + Es Teh"
   untuk mendongkrak keduanya sekaligus.
3. Evaluasi menu rendah: Teh Hangat hanya Rp459.000 total. Perlu dicek
   apakah karena sepi peminat atau jarang tersedia — jika sepi, bisa
   dikurangi porsi produksinya atau diganti menu baru.
4. Penjadwalan & SDM: jam/transaksi dengan Nasi Goreng tinggi butuh
   juru masak dan kompor lebih banyak agar antrean tidak menumpuk.
""")
