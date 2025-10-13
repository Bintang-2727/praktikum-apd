# ==========================================
# Program: Toko Baju Brand
# Pembuat: Bintang Dhana Permadi
# ==========================================

import os

# --- Data awal ---
users = [
    ["admin", "admin123", "admin"],
    ["udin", "1234", "user"]
]

produk = [
    ["Kaos Lacoste", 250000],
    ["Celana Rucas", 400000],
    ["Jaket H&M", 550000],
    ["Topi Nike", 150000],
    ["Sepatu Adidas", 750000],
]

# --- Program utama ---
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SELAMAT DATANG DI TOKO BAJU BRAND ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    # --- LOGIN ---
    if pilih == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        akun = None
        for user in users:
            if user[0] == username and user[1] == password:
                akun = user
                break

        if akun is None:
            print("Login gagal! Username atau password salah.")
            input("Tekan Enter untuk kembali...")
        else:
            print(f"Login berhasil sebagai {akun[2].upper()}!")
            input("Tekan Enter untuk melanjutkan...")

            # =================== ADMIN ===================
            if akun[2] == "admin":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== MENU ADMIN TOKO BAJU BRAND ===")
                    print("1. Lihat Produk")
                    print("2. Tambah Produk")
                    print("3. Update Produk")
                    print("4. Hapus Produk")
                    print("5. Logout")
                    menu_admin = input("Pilih menu: ")

                    # --- Lihat Produk ---
                    if menu_admin == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR PRODUK ===")
                        if len(produk) == 0:
                            print("Belum ada produk.")
                        else:
                            for i in range(len(produk)):
                                print(f"{i+1}. {produk[i][0]} - Rp{produk[i][1]:,}")
                        input("\nTekan Enter untuk kembali...")

                    # --- Tambah Produk ---
                    elif menu_admin == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        nama = input("Masukkan nama produk: ").strip()
                        harga = input("Masukkan harga produk: ").strip()

                        if nama == "" or harga == "":
                            print("Nama dan harga tidak boleh kosong!")
                        elif not all(h in "0123456789" for h in harga):
                            print("Harga harus berupa angka!")
                        else:
                            produk.append([nama, int(harga)])
                            print(f"Produk '{nama}' berhasil ditambahkan!")
                        input("\nTekan Enter untuk kembali...")

                    # --- Update Produk ---
                    elif menu_admin == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== UBAH PRODUK ===")
                        for i in range(len(produk)):
                            print(f"{i+1}. {produk[i][0]} - Rp{produk[i][1]:,}")

                        index = input("\nMasukkan nomor produk yang ingin diubah: ")

                        if index != "" and all(ch in "0123456789" for ch in index):
                            index = int(index) - 1
                            if 0 <= index < len(produk):
                                nama_baru = input("Nama baru (kosongkan jika tidak diubah): ").strip()
                                harga_baru = input("Harga baru (kosongkan jika tidak diubah): ").strip()
                                if nama_baru != "":
                                    produk[index][0] = nama_baru
                                if harga_baru != "" and all(h in "0123456789" for h in harga_baru):
                                    produk[index][1] = int(harga_baru)
                                print("Produk berhasil diperbarui!")
                            else:
                                print("Nomor produk tidak ditemukan!")
                        else:
                            print("Input tidak valid!")
                        input("\nTekan Enter untuk kembali...")

                    # --- Hapus Produk ---
                    elif menu_admin == "4":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== HAPUS PRODUK ===")
                        for i in range(len(produk)):
                            print(f"{i+1}. {produk[i][0]} - Rp{produk[i][1]:,}")

                        index = input("\nMasukkan nomor produk yang ingin dihapus: ")

                        if index != "" and all(ch in "0123456789" for ch in index):
                            index = int(index) - 1
                            if 0 <= index < len(produk):
                                hapus = produk.pop(index)
                                print(f"Produk '{hapus[0]}' berhasil dihapus.")
                            else:
                                print("Nomor produk tidak ditemukan!")
                        else:
                            print("Input tidak valid!")
                        input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "5":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("\nTekan Enter untuk kembali...")

            # =================== USER ===================
            else:
                keranjang = []
                total = 0
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"=== SELAMAT DATANG {akun[0].upper()} DI TOKO BAJU BRAND ===")
                    for i in range(len(produk)):
                        print(f"{i+1}. {produk[i][0]} - Rp{produk[i][1]:,}")
                    print("0. Checkout")

                    pilih_user = input("\nPilih produk: ")

                    if pilih_user == "0":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== STRUK BELANJA ===")
                        for item in keranjang:
                            print(f"- {item[0]} : Rp{item[1]:,}")
                        print("------------------------------")
                        print(f"Total belanja : Rp{total:,}")
                        print("Terima kasih telah berbelanja!\n")
                        input("Tekan Enter untuk keluar...")
                        break

                    elif pilih_user != "" and all(ch in "0123456789" for ch in pilih_user):
                        pilih_user = int(pilih_user) - 1
                        if 0 <= pilih_user < len(produk):
                            keranjang.append(produk[pilih_user])
                            total += produk[pilih_user][1]
                            print(f"{produk[pilih_user][0]} berhasil ditambahkan ke keranjang!")
                        else:
                            print("Produk tidak ditemukan!")
                    else:
                        print("Input tidak valid!")
                    input("\nTekan Enter untuk lanjut...")

    # --- REGISTER ---
    elif pilih == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        username = input("Buat username: ").strip()
        password = input("Buat password: ").strip()

        duplikat = False
        for user in users:
            if user[0] == username:
                duplikat = True
                break

        if duplikat:
            print("Username sudah digunakan!")
        elif username == "" or password == "":
            print("Username dan password tidak boleh kosong!")
        else:
            users.append([username, password, "user"])
            print("Akun berhasil dibuat! Silakan login.")
        input("\nTekan Enter untuk kembali...")

    # --- KELUAR ---
    elif pilih == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah mengunjungi Toko Baju Brand!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")