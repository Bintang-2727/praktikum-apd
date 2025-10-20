import os

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "udin": {"password": "1234", "role": "user"}
}

produk = {
    1: {"nama": "Kaos Lacoste", "harga": 250000},
    2: {"nama": "Celana Rucas", "harga": 400000},
    3: {"nama": "Jaket H&M", "harga": 550000},
    4: {"nama": "Topi Nike", "harga": 150000},
    5: {"nama": "Sepatu Adidas", "harga": 750000}
}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SELAMAT DATANG DI TOKO BAJU BRAND ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Login berhasil sebagai {role.upper()}!")
            input("Tekan Enter untuk melanjutkan...")

            if role == "admin":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== MENU ADMIN TOKO BAJU BRAND ===")
                    print("1. Lihat Produk")
                    print("2. Tambah Produk")
                    print("3. Update Produk")
                    print("4. Hapus Produk")
                    print("5. Logout")
                    menu_admin = input("Pilih menu: ")

                    if menu_admin == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR PRODUK ===")
                        if len(produk) == 0:
                            print("Belum ada produk.")
                        else:
                            for id_p, data in produk.items():
                                print(f"{id_p}. {data['nama']} - Rp{data['harga']:,}")
                        input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        nama = input("Masukkan nama produk: ").strip()
                        harga = input("Masukkan harga produk: ").strip()

                        if nama == "" or harga == "":
                            print("Nama dan harga tidak boleh kosong!")
                        elif not all(h.isdigit() for h in harga):
                            print("Harga harus berupa angka!")
                        else:
                            id_baru = max(produk.keys()) + 1 if len(produk) > 0 else 1
                            produk[id_baru] = {"nama": nama, "harga": int(harga)}
                            print(f"Produk '{nama}' berhasil ditambahkan!")
                        input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== UBAH PRODUK ===")
                        for id_p, data in produk.items():
                            print(f"{id_p}. {data['nama']} - Rp{data['harga']:,}")

                        index = input("\nMasukkan nomor produk yang ingin diubah: ")
                        if index.isdigit() and int(index) in produk:
                            index = int(index)
                            nama_baru = input("Nama baru (kosongkan jika tidak diubah): ").strip()
                            harga_baru = input("Harga baru (kosongkan jika tidak diubah): ").strip()
                            if nama_baru != "":
                                produk[index]["nama"] = nama_baru
                            if harga_baru != "" and harga_baru.isdigit():
                                produk[index]["harga"] = int(harga_baru)
                            print("Produk berhasil diperbarui!")
                        else:
                            print("Nomor produk tidak ditemukan atau input salah!")
                        input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "4":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== HAPUS PRODUK ===")
                        for id_p, data in produk.items():
                            print(f"{id_p}. {data['nama']} - Rp{data['harga']:,}")

                        index = input("\nMasukkan nomor produk yang ingin dihapus: ")
                        if index.isdigit() and int(index) in produk:
                            hapus = produk.pop(int(index))
                            print(f"Produk '{hapus['nama']}' berhasil dihapus.")
                        else:
                            print("Nomor produk tidak ditemukan!")
                        input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "5":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("\nTekan Enter untuk kembali...")

            else:
                keranjang = []
                total = 0
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"=== SELAMAT DATANG {username.upper()} DI TOKO BAJU BRAND ===")
                    for id_p, data in produk.items():
                        print(f"{id_p}. {data['nama']} - Rp{data['harga']:,}")
                    print("0. Checkout")

                    pilih_user = input("\nPilih produk: ")

                    if pilih_user == "0":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== STRUK BELANJA ===")
                        for item in keranjang:
                            print(f"- {item['nama']} : Rp{item['harga']:,}")
                        print("------------------------------")
                        print(f"Total belanja : Rp{total:,}")
                        print("Terima kasih telah berbelanja!\n")
                        input("Tekan Enter untuk keluar...")
                        break

                    elif pilih_user.isdigit() and int(pilih_user) in produk:
                        item = produk[int(pilih_user)]
                        keranjang.append(item)
                        total += item["harga"]
                        print(f"{item['nama']} berhasil ditambahkan ke keranjang!")
                    else:
                        print("Input tidak valid!")
                    input("\nTekan Enter untuk lanjut...")

        else:
            print("Login gagal! Username atau password salah.")
            input("Tekan Enter untuk kembali...")

    elif pilih == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        username = input("Buat username: ").strip()
        password = input("Buat password: ").strip()

        if username in users:
            print("Username sudah digunakan!")
        elif username == "" or password == "":
            print("Username dan password tidak boleh kosong!")
        else:
            users[username] = {"password": password, "role": "user"}
            print("Akun berhasil dibuat! Silakan login.")
        input("\nTekan Enter untuk kembali...")

    elif pilih == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah mengunjungi Toko Baju Brand!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
