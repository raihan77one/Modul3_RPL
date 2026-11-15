from models.anggota_model import AnggotaModel

model = AnggotaModel()

# Menambahkan beberapa data anggota baru ke tabel anggota
print("Menambahkan data anggota perpustakaan...")
model.create_anggota("Raihan Irbah Zaki", "Jl. Soekarno Hatta, Palu")
model.create_anggota("Hasby Pratama", "Jl. Towua, Palu")
model.create_anggota("Akbar Saputra", "Jl. Garuda, Palu")
print("Data anggota berhasil disimpan!\n")

# Menampilkan seluruh daftar anggota dari database
print("=== Daftar Anggota Perpustakaan ===")
daftar_anggota = model.get_all_anggota()
for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")