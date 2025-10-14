# praktikum = ['APD', 'orsikom', 'jarkom', 'rpl']




# Ruang = praktikum.pop()
# print(praktikum)
# praktikum.append('matdis')

# angka = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# kombinasi = huruf * 3
# print(kombinasi)

# list mahasiswa
# mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# # perulangan for untuk mendapatkan semua elemen
# for i in mahasiswa:
#     for j in i :
#         print (j)

# # i dan j merupakan variabel sementara / temporary, kita dapat menggantinya
# #dengan apa saja asal sesuai dengan syarat nama variabel

# # output
# Daffa
# Dante
# Santoso
# Pernanda
# Triya
# Ahnaf

import os

# Data login awal
users = [['admin', 'admin123', 'admin']]
# Data menu warung padang: [nama_menu, harga, kategori]
menu_warung = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== List Daftar Menu Warung Padang ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    # LOGIN
    if pilihan == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Login ===")
        username = input("Username: ")
        password = input("Password: ")
        login_sukses = False
        for user in users:
            if user[0] == username and user[1] == password:
                login_sukses = True
                role = user[2]
                break
        if not login_sukses:
            print("❌ Username atau password salah.")
            input("Tekan Enter untuk lanjut...")
            continue

        # MENU ADMIN
        while role == 'admin':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Menu Admin Warung Padang ===")
            print("1. Lihat Menu")
            print("2. Tambah Menu")
            print("3. Ubah Menu")
            print("4. Hapus Menu")
            print("5. Logout")
            menu = input("Pilih menu: ")

            # Lihat Menu
            if menu == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== Daftar Menu ===")
                if len(menu_warung) == 0:
                    print("📭 Belum ada menu.")
                else:
                    for i, item in enumerate(menu_warung):
                        print(f"{i+1}. {item[0]} - Rp{item[1]} ({item[2]})")
                input("Tekan Enter untuk kembali...")

            # Tambah Menu
            elif menu == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== Tambah Menu Baru ===")
                nama = input("Nama Menu: ")
                harga = input("Harga: ")
                kategori = input("Kategori (makanan/minuman): ")
                if nama and harga.isdigit() and kategori:
                    menu_warung.append([nama, int(harga), kategori])
                    print("✅ Menu berhasil ditambahkan.")
                else:
                    print("❌ Data tidak valid.")
                input("Tekan Enter untuk kembali...")

            # Ubah Menu
            elif menu == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== Ubah Menu ===")
                for i, item in enumerate(menu_warung):
                    print(f"{i+1}. {item[0]} - Rp{item[1]} ({item[2]})")
                index = input("Nomor menu yang ingin diubah: ")
                if index.isdigit():
                    idx = int(index) - 1
                    if 0 <= idx < len(menu_warung):
                        nama = input("Nama baru: ")
                        harga = input("Harga baru: ")
                        kategori = input("Kategori baru: ")
                        if nama and harga.isdigit() and kategori:
                            menu_warung[idx] = [nama, int(harga), kategori]
                            print("✅ Menu berhasil diubah.")
                        else:
                            print("❌ Data tidak valid.")
                    else:
                        print("❌ Nomor menu tidak ditemukan.")
                else:
                    print("❌ Input harus angka.")
                input("Tekan Enter untuk kembali...")

            # Hapus Menu
            elif menu == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== Hapus Menu ===")
                for i, item in enumerate(menu_warung):
                    print(f"{i+1}. {item[0]} - Rp{item[1]} ({item[2]})")
                index = input("Nomor menu yang ingin dihapus: ")
                if index.isdigit():
                    idx = int(index) - 1
                    if 0 <= idx < len(menu_warung):
                        del menu_warung[idx]
                        print("✅ Menu berhasil dihapus.")
                    else:
                        print("❌ Nomor menu tidak ditemukan.")
                else:
                    print("❌ Input harus angka.")
                input("Tekan Enter untuk kembali...")

            # Logout
            elif menu == '5':
                break
            else:
                print("❌ Menu tidak valid.")
                input("Tekan Enter untuk lanjut...")

        # MENU USER
        while role == 'user':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Menu Pengguna Warung Padang ===")
            print("1. Lihat Menu")
            print("2. Logout")
            menu = input("Pilih menu: ")

            if menu == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== Daftar Menu ===")
                if len(menu_warung) == 0:
                    print("📭 Belum ada menu.")
                else:
                    for i, item in enumerate(menu_warung):
                        print(f"{i+1}. {item[0]} - Rp{item[1]} ({item[2]})")
                input("Tekan Enter untuk kembali...")
            elif menu == '2':
                break
            else:
                print("❌ Menu tidak valid.")
                input("Tekan Enter untuk lanjut...")

    # REGISTER
    elif pilihan == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Registrasi Pengguna Baru ===")
        username = input("Username: ")
        password = input("Password: ")
        role = 'user'
        sudah_ada = False
        for user in users:
            if user[0] == username:
                sudah_ada = True
                break
        if sudah_ada:
            print("❌ Username sudah digunakan.")
        else:
            users.append([username, password, role])
            print("✅ Registrasi berhasil!")
        input("Tekan Enter untuk lanjut...")

    # KELUAR
    elif pilihan == '3':
        print("👋 Keluar dari program.")
        break

    else:
        print("❌ Menu tidak valid.")
        input("Tekan Enter untuk lanjut...")