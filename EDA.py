import pandas as pd
df = pd.read_csv("KKA-Modul2/data_penjualan_bersih.csv")

# Menampilkan 5 baris teratas
print("Menampilkan 5 Baris Teratas:")
print(df.head())

# Menampilkan informasi tentang DataFrame
print("\nInformasi DataFrame:")
df.info()

# Menampilkan ringkasan statistik DataFrame
print("\nRingkasan Statistik DataFrame:")
print(df.describe())

# Menampilkan jumlah baris dan kolom DataFrame
print("\nShape:", df.shape)

# Mengecek missing value
print("\nMissing Value:")
print(df.isnull().sum())

# Mengecek data duplikat
print("\nJumlah Data Duplikat:", df.duplicated().sum())

# ===== DATA CLEANING =====

# 1. Menangani outlier pada jumlah_terjual (500 dianggap salah input, diganti median)
df.loc[df['jumlah_terjual'] == 500, 'jumlah_terjual'] = df['jumlah_terjual'].median()

# 2. Menangani missing value pada jumlah_terjual
# Teknik: dropna (bukan fillna), karena hanya 4 dari 65 baris (~6%) yang kosong,
# dan mengisi dengan nilai tebakan berisiko mendistorsi hasil groupby/agregasi nanti
df = df.dropna(subset=['jumlah_terjual'])

# 3. Memperbaiki tipe data kolom tanggal (dari str/object menjadi datetime)
df['tanggal'] = pd.to_datetime(df['tanggal'])

# 4. Verifikasi hasil cleaning
print("\n=== Verifikasi Setelah Cleaning ===")
print("Missing value:\n", df.isnull().sum())
print("\nJumlah duplikat:", df.duplicated().sum())
print("\nShape:", df.shape)
df.info()


# ===== DATA MANIPULATION =====

# 1. Kolom turunan: total pendapatan per transaksi (jumlah_terjual x harga_satuan)
df['total_pendapatan'] = df['jumlah_terjual'] * df['harga_satuan']

# 2. Filtering: hanya transaksi kategori "Makanan"
df_makanan = df[df['kategori'] == 'Makanan']
print("\nTransaksi kategori Makanan:")
print(df_makanan.head())

# 3. Sorting: urutkan transaksi berdasarkan total_pendapatan tertinggi
df_sorted = df.sort_values(by='total_pendapatan', ascending=False)
print("\n5 Transaksi dengan Pendapatan Tertinggi:")
print(df_sorted.head())

# 4. Groupby/agregasi: total pendapatan per nama_produk
pendapatan_per_produk = df.groupby('nama_produk')['total_pendapatan'].sum().sort_values(ascending=False)
print("\nTotal Pendapatan per Produk:")
print(pendapatan_per_produk)

df.to_csv('KKA-Modul2/dataset_bersih.csv', index=False)
print("\nDataset bersih berhasil disimpan.")

# ============================================================
# DATA PROFILING SUMMARY
# ============================================================
#
# Temuan 1: Produk dengan Pendapatan Tertinggi
# Nasi Goreng adalah produk dengan kontribusi pendapatan
# tertinggi (Rp876.000), jauh melampaui produk kedua yaitu
# Mie Ayam (Rp510.000) - selisihnya hampir 72%. Ini menunjukkan
# Nasi Goreng menjadi produk andalan yang sebaiknya
# diprioritaskan stok bahan bakunya.
#
# Temuan 2: Transaksi dengan Pendapatan Tertinggi
# Transaksi dengan pendapatan tertinggi (Rp180.000) juga
# berasal dari produk Nasi Goreng, memperkuat bahwa produk ini
# konsisten menjadi penyumbang pendapatan terbesar, baik dari
# sisi total maupun transaksi individual.
#
# Temuan 3: Anomali Data pada Transaksi Roti Bakar
# Ditemukan 1 kejanggalan data (outlier) pada transaksi
# Roti Bakar dengan jumlah terjual tercatat 500 porsi dalam
# satu transaksi - jauh di luar pola normal (1-15 porsi).
# Setelah dikoreksi menggunakan nilai median, data ini tidak
# lagi mendistorsi hasil analisis pendapatan per produk.
#
# ============================================================