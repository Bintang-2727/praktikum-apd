from utils import clear_screen, tampilkan_header
from data import users
from admin import tambah_produk, ubah_produk, hapus_produk
from user import menu_user
from utils import tampilkan_produk
from data import produk

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
                    print("3. Ubah Produk")
                    print("4. Hapus Produk")
                    print("5. Logout")
                    menu_admin = input("Pilih menu: ")

                    if menu_admin == "1":
                        clear_screen()
                        tampilkan_produk(produk)
                        input("\nTekan Enter untuk kembali...")
                    elif menu_admin == "2":
                        tambah_produk()
                        input("\nTekan Enter untuk kembali...")
                    elif menu_admin == "3":
                        ubah_produk()
                        input("\nTekan Enter untuk kembali...")
                    elif menu_admin == "4":
                        hapus_produk()
                        input("\nTekan Enter untuk kembali...")
                    elif menu_admin == "5":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("\nTekan Enter untuk kembali...")
            else:
                menu_user(username)
        else:
            print("Login gagal! Username atau password salah.")
            input("\nTekan Enter untuk kembali...")

    elif pilih == "2":
        clear_screen()
        print("=== REGISTER AKUN BARU ===")
        username = input("Buat username: ").strip()
        password = input("Buat password: ").strip()

        if username in users:
            print("Username sudah digunakan!")
        elif not username or not password:
            print("Username dan password tidak boleh kosong!")
        else:
            users[username] = {"password": password, "role": "user"}
            print("Akun berhasil dibuat! Silakan login.")
        input("\nTekan Enter untuk kembali...")

    elif pilih == "3":
        clear_screen()
        print("Terima kasih telah mengunjungi Toko Baju Brand!")
        break

    else:
        print("Pilihan tidak valid!")
        input("\nTekan Enter untuk kembali...")
