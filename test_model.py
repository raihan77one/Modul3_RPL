from models.buku_model import BukuModel

model = BukuModel()

# Menguji fungsi Update (ganti angka 1 dengan id_buku yang ada di databasemu)
print("Mengubah data buku...")
model.update_buku(1, "Pemrograman Python MVC V2", "Guido van Rossum", 2024)
print("Data berhasil diubah!")

# Menguji fungsi Delete (ganti angka 2 dengan id_buku yang ingin dihapus)
print("Menghapus data buku...")
model.delete_buku(2)
print("Data berhasil dihapus!")

# Menampilkan daftar buku setelah diubah dan dihapus
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")