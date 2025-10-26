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

keranjang_global = [] 


def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def tampilkan_header():
    """Menampilkan header toko."""
    print("=== SELAMAT DATANG DI TOKO BAJU BRAND ===")


def tambah_produk(id_baru, nama, harga):
    """Menambahkan produk baru ke dalam dictionary produk."""
    global produk
    produk[id_baru] = {"nama": nama, "harga": harga}
    print(f"Produk '{nama}' berhasil ditambahkan!")


def hitung_total(keranjang):
    """Menghitung total harga dari semua produk di keranjang."""
    total = 0  
    for item in keranjang:
        total += item["harga"]
    return total


def tampilkan_produk_recursive(keys, index=0):
    """Menampilkan produk secara rekursif."""
    if index >= len(keys):
        return
    key = keys[index]
    data = produk[key]
    print(f"{key}. {data['nama']} - Rp{data['harga']:,}")
    tampilkan_produk_recursive(keys, index + 1)


def daftar_produk():
    """Prosedur untuk menampilkan daftar produk."""
    clear_screen()
    print("=== DAFTAR PRODUK ===")
    if len(produk) == 0:
        print("Belum ada produk.")
    else:
        keys = list(produk.keys())
        tampilkan_produk_recursive(keys)
    input("\nTekan Enter untuk kembali...")


def struk_belanja(keranjang):
    """Menampilkan struk belanja (prosedur tanpa return)."""
    clear_screen()
    print("=== STRUK BELANJA ===")
    for item in keranjang:
        print(f"- {item['nama']} : Rp{item['harga']:,}")
    total = hitung_total(keranjang)
    print("------------------------------")
    print(f"Total belanja : Rp{total:,}")
    print("Terima kasih telah berbelanja!\n")
    input("Tekan Enter untuk keluar...")


while True:
    clear_screen()
    tampilkan_header()
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        clear_screen()
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Login berhasil sebagai {role.upper()}!")
            input("Tekan Enter untuk melanjutkan...")

            if role == "admin":
                while True:
                    clear_screen()
                    print("=== MENU ADMIN ===")
                    print("1. Lihat Produk")
                    print("2. Tambah Produk")
                    print("3. Update Produk")
                    print("4. Hapus Produk")
                    print("5. Logout")
                    menu_admin = input("Pilih menu: ")

                    try:
                        if menu_admin == "1":
                            daftar_produk()

                        elif menu_admin == "2":
                            clear_screen()
                            print("=== TAMBAH PRODUK ===")
                            nama = input("Masukkan nama produk: ").strip()
                            harga = input("Masukkan harga produk: ").strip()

                            if nama == "" or harga == "":
                                print("Nama dan harga tidak boleh kosong!")
                            elif not harga.isdigit():
                                print("Harga harus berupa angka!")
                            else:
                                id_baru = max(produk.keys()) + 1 if len(produk) > 0 else 1
                                tambah_produk(id_baru, nama, int(harga))
                            input("\nTekan Enter untuk kembali...")

                        elif menu_admin == "3":
                            clear_screen()
                            print("=== UBAH PRODUK ===")
                            daftar_produk()
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
                                print("Nomor produk tidak ditemukan!")
                            input("\nTekan Enter untuk kembali...")

                        elif menu_admin == "4":
                            clear_screen()
                            print("=== HAPUS PRODUK ===")
                            daftar_produk()
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
                    except Exception as e:
                        print(f"Terjadi kesalahan: {e}")
                        input("\nTekan Enter untuk kembali...")

            else:  
                keranjang_global.clear()
                while True:
                    clear_screen()
                    print(f"=== MENU PENGGUNA: {username.upper()} ===")
                    keys = list(produk.keys())
                    tampilkan_produk_recursive(keys)
                    print("0. Checkout")

                    pilih_user = input("\nPilih produk: ")

                    try:
                        if pilih_user == "0":
                            struk_belanja(keranjang_global)
                            break
                        elif pilih_user.isdigit() and int(pilih_user) in produk:
                            item = produk[int(pilih_user)]
                            keranjang_global.append(item)
                            print(f"{item['nama']} berhasil ditambahkan ke keranjang!")
                        else:
                            print("Input tidak valid!")
                        input("\nTekan Enter untuk lanjut...")
                    except Exception as e:
                        print(f"Terjadi kesalahan: {e}")
                        input("\nTekan Enter untuk lanjut...")

        else:
            print("Login gagal! Username atau password salah.")
            input("Tekan Enter untuk kembali...")

    elif pilih == "2":
        clear_screen()
        print("=== REGISTER AKUN BARU ===")
        username = input("Buat username: ").strip()
        password = input("Buat password: ").strip()

        try:
            if username in users:
                print("Username sudah digunakan!")
            elif username == "" or password == "":
                print("Username dan password tidak boleh kosong!")
            else:
                users[username] = {"password": password, "role": "user"}
                print("Akun berhasil dibuat! Silakan login.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
        input("\nTekan Enter untuk kembali...")

    elif pilih == "3":
        clear_screen()
        print("Terima kasih telah mengunjungi Toko Baju Brand!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
