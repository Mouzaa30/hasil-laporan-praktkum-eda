# 1. DATA LOADING & INSPECTION
import io
import pandas as pd

# Load dataset dari string CSV
csv_data = """id_transaksi,tanggal,nama_produk,kategori,jumlah_terjual,harga_satuan,nama_kasir,metode_pembayaran
TRX0042,2026-08-11,Roti Bakar,Makanan,9,7000,Pak Agus,Tunai
TRX0005,2026-08-03,Gorengan,makanan,2,2000,Bu Sri,QRIS
TRX0011,2026-08-04,Jus Alpukat,Minuman,4,,Bu Wati,Tunai
TRX0035,2026-08-10,Mie Ayam,Makanan,,10000,Pak Joko,Transfer
TRX0007,2026-08-03,Kerupuk,Snack,10,Rp2.000,Bu Wati,Transfer
TRX0045,2026-08-11,Teh Botol,Minuman,9,5000,Pak Joko,QRIS
TRX0061,14 Agustus 2026,Teh Botol,MINUMAN,14,5000,Bu Sri,QRIS
TRX0008,4 Agustus 2026,Mie Ayam,makanan,14,10000,Pak Joko,Tunai
TRX0031,7 Agustus 2026,Nasi Goreng,makanan,,12000,Pak Agus,Tunai
TRX0057,13/08/2026,Jus Alpukat,MINUMAN,14,8000,Bu Sri,Tunai
TRX0017,2026-08-05,Es Jeruk,Minuman,1,4000,Bu Wati,Transfer
TRX0052,2026-08-12,Roti Bakar,Makanan,3,7000,Bu Wati,Tunai
TRX0047,2026-08-12,Teh Botol,MINUMAN,12 pcs,5000,Pak Joko,QRIS
TRX0015,5 Agustus 2026,Kerupuk,Snack,7,2000,Bu Sri,QRIS
TRX0048,2026-08-12,Keripik Singkong,snack,15,Rp3.000,Bu Wati,QRIS
TRX0004,03/08/2026,Nasi Goreng,makanan,13,Rp12.000,Pak Joko,QRIS
TRX0054,13 Agustus 2026,Jus Alpukat,Minuman,15,8000,Pak Joko,Tunai
TRX0014,2026-08-05,Bakso,Makanan,9,Rp11.000,Pak Agus,Tunai
TRX0026,7 Agustus 2026,Teh Botol,MINUMAN,8,Rp5.000,Pak Joko,QRIS
TRX0034,2026-08-10,Bakso,Makanan,1,11000,Bu Sri,QRIS
TRX0046,2026-08-11,Nasi Goreng,Makanan,15,12000,Bu Wati,QRIS
TRX0003,3 Agustus 2026,Nasi Goreng,MAKANAN,9,12000,Pak Joko,Transfer
TRX0025,6 Agustus 2026,Mie Ayam,MAKANAN,9,10000,Pak Joko,Tunai
TRX0019,2026-08-06,Nasi Goreng,Makanan,10,12000,Bu Wati,QRIS
TRX0012,4 Agustus 2026,Mie Ayam,Makanan,4,10000,Bu Wati,QRIS
TRX0032,2026-08-07,Roti Bakar,makanan,7 pcs,Rp7.000,Pak Agus,QRIS
TRX0059,14/08/2026,Bakso,Makanan,11,11000,Bu Sri,Tunai
TRX0055,13/08/2026,Teh Botol,Minuman,6,5000,Bu Sri,Tunai
TRX0043,11/08/2026,Nasi Goreng,MAKANAN,1,,Bu Wati,QRIS
TRX0029,2026-08-07,Nasi Uduk,Makanan,14,8000,Bu Sri,QRIS
TRX0051,12 Agustus 2026,Mie Ayam,makanan,13 pcs,10000,Bu Wati,Tunai
TRX0060,2026-08-14,Kerupuk,Snack,5,Rp2.000,Pak Joko,QRIS
TRX0006,2026-08-03,Nasi Goreng,Makanan,12,Rp12.000,Pak Agus,Transfer
TRX0027,2026-08-07,Gorengan,Makanan,7,Rp2.000,Pak Agus,QRIS
TRX0023,06/08/2026,Mie Ayam,Makanan,4,10000,Pak Joko,Tunai
TRX0020,2026-08-06,Roti Bakar,Makanan,4,7000,,QRIS
TRX0062,2026-08-14,Es Teh,Minuman,4,Rp3.000,Pak Joko,Tunai
TRX0022,6 Agustus 2026,Es Teh,minuman,4,3000,Pak Joko,Tunai
TRX0033,2026-08-10,Jus Alpukat,Minuman,1,8000,Bu Wati,Tunai
TRX0010,4 Agustus 2026,Keripik Singkong,snack,,3000,Pak Joko,QRIS
TRX0018,05/08/2026,Kerupuk,SNACK,9,2000,,QRIS
TRX0037,2026-08-10,Kerupuk,Snack,,2000,Pak Agus,Tunai
TRX0038,10/08/2026,Mie Ayam,MAKANAN,2,10000,Pak Joko,Transfer
TRX0028,7 Agustus 2026,Mie Ayam,MAKANAN,4,10000,Pak Joko,QRIS
TRX0016,05/08/2026,Nasi Goreng,makanan,11,Rp12.000,Bu Sri,Transfer
TRX0040,2026-08-11,Jus Alpukat,minuman,1 pcs,Rp8.000,Bu Wati,Tunai
TRX0021,6 Agustus 2026,Jus Alpukat,MINUMAN,13,8000,Pak Joko,QRIS
TRX0009,04/08/2026,Bakso,Makanan,6,11000,Bu Wati,QRIS
TRX0028,7 Agustus 2026,Mie Ayam,MAKANAN,4,10000,Pak Joko,QRIS
TRX0013,04/08/2026,Bakso,Makanan,5,11000,Pak Joko,QRIS
TRX0001,2026-08-03,Mie Ayam,MAKANAN,1,10000,Bu Wati,QRIS
TRX0003,3 Agustus 2026,Nasi Goreng,MAKANAN,9,12000,Pak Joko,Transfer
TRX0063,2026-08-14,Keripik Singkong,Snack,9,3000,Pak Agus,Tunai
TRX0065,14/08/2026,Es Jeruk,Minuman,8,4000,Bu Wati,QRIS
TRX0044,2026-08-11,Es Teh,MINUMAN,9,3000,Bu Sri,Tunai
TRX0039,10 Agustus 2026,Nasi Uduk,makanan,6,8000,Bu Wati,QRIS
TRX0030,7 Agustus 2026,Nasi Goreng,Makanan,2,12000,,QRIS
TRX0049,2026-08-12,Es Teh,MINUMAN,14,3000,Bu Sri,QRIS
TRX0064,14 Agustus 2026,Kerupuk,Snack,9,2000,Bu Wati,QRIS
TRX0050,2026-08-12,Roti Bakar,MAKANAN,500,7000,Pak Joko,QRIS
TRX0056,13 Agustus 2026,Jus Alpukat,MINUMAN,3,8000,Pak Joko,QRIS
TRX0042,2026-08-11,Roti Bakar,Makanan,9,7000,Pak Agus,Tunai
TRX0024,2026-08-06,Nasi Uduk,Makanan,1,8000,Bu Sri,Tunai
TRX0057,13/08/2026,Jus Alpukat,MINUMAN,14,8000,Bu Sri,Tunai
TRX0053,2026-08-13,Teh Botol,minuman,9,Rp5.000,Bu Sri,QRIS
TRX0041,2026-08-11,Jus Alpukat,minuman,3,,Bu Wati,Tunai
TRX0058,13 Agustus 2026,Kerupuk,SNACK,6,2000,Pak Agus,QRIS
TRX0036,10/08/2026,Jus Alpukat,MINUMAN,6 pcs,8000,Bu Wati,QRIS
TRX0002,2026-08-03,Jus Alpukat,Minuman,2,Rp8.000,Pak Agus,Tunai"""

df = pd.read_csv(io.StringIO(csv_data))

print("=== HEAD ===")
print(df.head())
print("\n=== INFO ===")
print(df.info())
print("\n=== DESCRIBE ===")
print(df.describe(include="all"))
print("\n=== SHAPE ===")
print(df.shape)

# 2. DATA CLEANING

# 2.1 Hapus Duplikat
# Alasan: Baris duplikat identik dihilangkan agar perhitungan finansial tidak double-count.
df = df.drop_duplicates()

# 2.2 Penanganan Teks dan Nilai Kosong pada Nama Kasir
# Alasan: Kapitalisasi disamakan (Title Case) dan kasir kosong diisi 'Tanpa Nama' agar tidak hilang saat agregasi.
df["kategori"] = df["kategori"].str.title()
df["nama_kasir"] = df["nama_kasir"].fillna("Tanpa Nama")

# 2.3 Standarisasi & Imputasi 'harga_satuan'
# Alasan: Menghapus 'Rp' dan titik, imputasi missing value menggunakan harga acuan per nama_produk.
df["harga_satuan"] = (
    df["harga_satuan"]
    .astype(str)
    .str.replace("Rp", "", regex=False)
    .str.replace(".", "", regex=False)
)
df["harga_satuan"] = pd.to_numeric(df["harga_satuan"], errors="coerce")
harga_lookup = df.groupby("nama_produk")["harga_satuan"].transform("median")
df["harga_satuan"] = df["harga_satuan"].fillna(harga_lookup)

# 2.4 Standarisasi & Handling Outlier pada 'jumlah_terjual'
# Alasan: Menghapus teks 'pcs', imputasi NaN dengan nilai 1. Outlier ekstrem (500) dikoreksi menjadi median (7) akibat typo input.
df["jumlah_terjual"] = (
    df["jumlah_terjual"]
    .astype(str)
    .str.replace(" pcs", "", regex=False)
    .str.strip()
)
df["jumlah_terjual"] = pd.to_numeric(df["jumlah_terjual"], errors="coerce")
df["jumlah_terjual"] = df["jumlah_terjual"].fillna(1)
df.loc[df["jumlah_terjual"] > 100, "jumlah_terjual"] = df.groupby(
    "nama_produk"
)["jumlah_terjual"].transform("median")

# 2.5 Parsing Tanggal
# Alasan: Menyelaraskan berbagai format tanggal ke tipe datetime standard (YYYY-MM-DD).
bulan_map = {
    "Agustus": "August",
    "Januari": "January",
    "Februari": "February",
    "Maret": "March",
    "April": "April",
    "Mei": "May",
    "Juni": "June",
    "Juli": "July",
    "September": "September",
    "Oktober": "October",
    "November": "November",
    "Desember": "December",
}
df_tgl = df["tanggal"].astype(str)
for id_b, en_b in bulan_map.items():
    df_tgl = df_tgl.str.replace(id_b, en_b, regex=False)
df["tanggal"] = pd.to_datetime(df_tgl, format="mixed", dayfirst=True)

# 2.6 Ubah tipe data ke Integer
df["jumlah_terjual"] = df["jumlah_terjual"].astype(int)
df["harga_satuan"] = df["harga_satuan"].astype(int)

# 3. DATA MANIPULATION

# 3.1 Feature Engineering (Kolom Turunan)
df["total_pendapatan"] = df["jumlah_terjual"] * df["harga_satuan"]

# 3.2 Filtering: Transaksi Makanan dengan nilai > Rp 50.000
filter_makanan_tinggi = df[
    (df["kategori"] == "Makanan") & (df["total_pendapatan"] > 50000)
]

# 3.3 Sorting: Urutkan transaksi berdasarkan Total Pendapatan tertinggi
df_sorted = df.sort_values(by="total_pendapatan", ascending=False)

# 3.4 Groupby & Agregasi: Performa Penjualan per Kasir
agregasi_kasir = (
    df.groupby("nama_kasir")
    .agg(
        total_transaksi=("id_transaksi", "count"),
        total_item_terjual=("jumlah_terjual", "sum"),
        total_pendapatan=("total_pendapatan", "sum"),
    )
    .reset_index()
)

# 4. EXPORT DATASET BERSIH
df.to_csv("dataset_bersih.csv", index=False)
print("\nDataset bersih berhasil disimpan ke 'dataset_bersih.csv'.")