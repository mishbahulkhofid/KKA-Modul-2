# KKA Modul 2 — EDA dengan NumPy & Pandas (Latihan 1–6)

Latihan bertahap Data Penjualan Kantin Sekolah: dari array dasar sampai dataset siap analisis.

## Struktur folder

```
latihan/
├── data_kantin.csv  # dataset mentah (110 baris)
├── latihan1.py      # Operasi dasar NumPy Array
├── latihan2.py      # Series & DataFrame
├── latihan3.py      # Data Loading & Inspection
├── latihan4.py      # Missing value (fillna / dropna)
├── latihan5.py      # Duplikat & tipe data
├── latihan6.py      # Filtering, sorting, groupby + kolom turunan
```

## Syarat

```bash
pip install numpy pandas
```

## Cara menjalankan

```bash
python3 latihan1.py
python3 latihan2.py
python3 latihan3.py
python3 latihan4.py
python3 latihan5.py
python3 latihan6.py
```

Setiap file mandiri (melakukan load + cleaning sendiri bila perlu) dan di akhir file mencetak jawaban **Tugas Analisis**.

## Ringkasan latihan & hasil

| File | Materi | Hasil pada `data_kantin.csv` |
|------|--------|------------------------------|
| 1 | `np.mean()`, `max()`, `median()`, `std()`, `array * 0.9` | List `[5000,7000,3000] * 0.9` → `TypeError`; NumPy vectorized tanpa loop |
| 2 | `pd.Series`, `pd.DataFrame` | `menu`: 1 kosong, `terjual`: 1 kosong; tanpa cleaning, `NaN` menular ke perhitungan |
| 3 | `read_csv`, `head()`, `info()`, `describe()`, `shape` | 110 baris; `menu` 107 non-null, `terjual` 104 non-null |
| 4 | `isnull().sum()`, `fillna(0)`, `dropna(subset=['menu'])` | `terjual` diisi 0 (numerik, aman), `menu` dibuang (identitas tak bisa ditebak); 110 → 107 baris |
| 5 | `duplicated().sum()`, `drop_duplicates()`, `astype(int)` | 5 duplikat; 107 → **102 baris**; `terjual` float→int |
| 6 | filter `terjual > 20`, `sort_values`, `harga * terjual`, `groupby('menu').sum()` | Tertinggi: **Nasi Goreng Rp3.924.000**, lalu Mie Ayam Rp2.410.000, Es Teh Rp2.144.000 |

## Alur EDA yang dipakai

Loading → Inspection → Cleaning (missing, duplikat, dtypes) → Manipulation (filter, sort, groupby, kolom turunan).
# KKA Modul 2 — EDA dengan NumPy & Pandas (Latihan 1–6)

Latihan bertahap Data Penjualan Kantin Sekolah: dari array dasar sampai dataset siap analisis.

## Struktur folder

```
latihan/
├── data_kantin.csv  # dataset mentah (110 baris)
├── latihan1.py      # Operasi dasar NumPy Array
├── latihan2.py      # Series & DataFrame
├── latihan3.py      # Data Loading & Inspection
├── latihan4.py      # Missing value (fillna / dropna)
├── latihan5.py      # Duplikat & tipe data
├── latihan6.py      # Filtering, sorting, groupby + kolom turunan
```

## Syarat

```bash
pip install numpy pandas
```

## Cara menjalankan

```bash
python3 latihan1.py
python3 latihan2.py
python3 latihan3.py
python3 latihan4.py
python3 latihan5.py
python3 latihan6.py
```

Setiap file mandiri (melakukan load + cleaning sendiri bila perlu) dan di akhir file mencetak jawaban **Tugas Analisis**.

## Ringkasan latihan & hasil

| File | Materi | Hasil pada `data_kantin.csv` |
|------|--------|------------------------------|
| 1 | `np.mean()`, `max()`, `median()`, `std()`, `array * 0.9` | List `[5000,7000,3000] * 0.9` → `TypeError`; NumPy vectorized tanpa loop |
| 2 | `pd.Series`, `pd.DataFrame` | `menu`: 1 kosong, `terjual`: 1 kosong; tanpa cleaning, `NaN` menular ke perhitungan |
| 3 | `read_csv`, `head()`, `info()`, `describe()`, `shape` | 110 baris; `menu` 107 non-null, `terjual` 104 non-null |
| 4 | `isnull().sum()`, `fillna(0)`, `dropna(subset=['menu'])` | `terjual` diisi 0 (numerik, aman), `menu` dibuang (identitas tak bisa ditebak); 110 → 107 baris |
| 5 | `duplicated().sum()`, `drop_duplicates()`, `astype(int)` | 5 duplikat; 107 → **102 baris**; `terjual` float→int |
| 6 | filter `terjual > 20`, `sort_values`, `harga * terjual`, `groupby('menu').sum()` | Tertinggi: **Nasi Goreng Rp3.924.000**, lalu Mie Ayam Rp2.410.000, Es Teh Rp2.144.000 |

## Alur EDA yang dipakai

Loading → Inspection → Cleaning (missing, duplikat, dtypes) → Manipulation (filter, sort, groupby, kolom turunan).
