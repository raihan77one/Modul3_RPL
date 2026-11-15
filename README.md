# Sistem Manajemen Perpustakaan (Desktop MVC)

Aplikasi desktop berbasis arsitektur **Model-View-Controller (MVC)** menggunakan bahasa pemrograman Python (`CustomTkinter`) yang terintegrasi dengan basis data **MySQL (Laragon)**. Aplikasi ini dilengkapi dengan fitur manajemen data buku dan anggota (CRUD), autentikasi pengguna menggunakan enkripsi **SHA-256**, pembatasan hak akses berbasis peran (**Role-Based Access Control / RBAC**), serta otomasi pengujian **CI/CD** melalui GitHub Actions.

## Struktur Direktori MVC

```text
modul3_rekayasa_perangkat_lunak/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml       # Konfigurasi CI GitHub Actions (Flake8 & Pytest)
├── config/
│   └── database.py               # Pengaturan koneksi basis data MySQL
├── controllers/
│   ├── anggota_controller.py     # Logika penghubung View dan Model Anggota
│   ├── auth_controller.py        # Logika proses Login dan pengalihan role
│   └── buku_controller.py        # Logika CRUD Buku dan otorisasi RBAC
├── models/
│   ├── anggota_model.py          # Operasi database tabel anggota
│   ├── buku_model.py             # Operasi database tabel buku
│   └── user_model.py             # Hashing SHA-256, autentikasi, dan registrasi user
├── tests/
│   ├── test_auth.py              # Unit test hashing & autentikasi
│   └── test_buku.py              # Unit test operasi data buku
├── views/
│   ├── anggota_view.py           # Antarmuka GUI pengelolaan anggota
│   ├── buku_view.py              # Antarmuka GUI pengelolaan buku
│   └── login_view.py             # Antarmuka GUI halaman login
├── .gitignore                    # Daftar file/folder yang diabaikan Git
├── main.py                       # Titik masuk utama (entry point) aplikasi
├── requirements.txt              # Daftar pustaka dependensi Python
└── README.md                     # Dokumentasi teknis proyek