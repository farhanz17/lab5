daftarkontak = {"Nama":"Nomor Telepon"}
kontak = {"Ari":"085883648213", "Dina":"085787653467"}

print("="*50)
print("   Nama          | Nomor Telepon ")
print("="*50)
print("  Ari      | ", kontak["Ari"])
print(" Dina   | ", kontak["Dina"])
print("-"*50)
print()
print()
print("="*50)

# Menampilkan Kontak Ari
print("Menampilkan kontak Hadeyal")
print("="*50)
print(" Ari      | ", kontak["Ari"])
print("-"*50)
print()
print()
print("="*50)

# Menampikan Kontak Dengan Nama Riko
print("Menambahkan kontak dengan Nama Aldi")
print("dengan nomor Telepon 085746372718")
kontak["Riko"]="085746372718"
print("="*50)
print(" Riko          | ", kontak["Riko"])
print("-"*50)
print()
print()
print("="*50)

# Mengubah Nomor Dina Dengan Nomor Baru
print("Mengubah Nomor Dina dengan Nomor 085781793926")
print("="*50)
print(" # Dina   | ", kontak["Dina"])
print("="*50)
print()
print()
print("="*50)

# Menampilkan Semua Nama
print("Menampilkan Semua Nama dalam Kontak")
print("="*50)
print(kontak.items())
print("-"*50)
print()
print()
print("="*50)

# Menampilkan Semua Nomor
print("Menampilkan Semua Nomor dalam Kontak")
print("="*50)
print(kontak.values())
print("-"*50)
print()
print()
print("="*50)

# Menampilkan Semua Daftar Kontak
print("Menampilkan Semua Daftar Kontak")
print("="*50)
print(kontak.items())
print("-"*50)
print()
print()
print("="*50)

# Menghapus salah satu Kontak
print("Hapus Kontak Riko")
print("="*50)
kontak.pop("Riko")
print(kontak.items())
print("-"*50)