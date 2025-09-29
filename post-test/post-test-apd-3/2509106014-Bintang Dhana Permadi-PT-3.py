print("=== Selamat Datang di Bintang Store ===")

member = input("Apakah Anda member? (ya/tidak): ").lower()
is_member = member == "ya"

if is_member:
    print("\n=== Login Member ===")
    username = input("Username: ")
    password = input("Password: ")

    login = True if (username == "udin" and password == "1234") else False

    if not login:
        print("Login gagal! Program berhenti.")
        exit()
    else:
        print("Login berhasil!\n")

print("\n=== Menu Produk ===")
print("1. Kaos Lacoste   - Rp250.000")
print("2. Celana Rucas - Rp400.000")
print("3. Jaket H&M  - Rp550.000")

pilih = int(input("Pilih produk (1-3): "))
jumlah = int(input("Jumlah: "))

if pilih == 1:
    total = 250000 * jumlah
    nama_produk = "Kaos Lacoste"
elif pilih == 2:
    total = 400000 * jumlah
    nama_produk = "Celana Rucas"
elif pilih == 3:
    total = 550000 * jumlah
    nama_produk = "Jaket H&M"
else:
    print("Produk tidak tersedia!")
    exit()

if is_member:
    diskon = total * 0.15
    total_setelah_diskon = total - diskon
    print("\n=== Struk Belanja Member ===")
    print(f"Produk             : {nama_produk}")
    print(f"Jumlah             : {jumlah}")
    print(f"Total sebelum diskon : Rp{total:,}")
    print(f"Diskon (15%)         : Rp{diskon:,}")
    print(f"Total setelah diskon : Rp{total_setelah_diskon:,}")
else:
    print("\n=== Struk Belanja Non-Member ===")
    print(f"Produk       : {nama_produk}")
    print(f"Jumlah       : {jumlah}")
    print(f"Total belanja: Rp{total:,}")

print("\nTerima kasih telah berbelanja di Toko Bintang Store")
