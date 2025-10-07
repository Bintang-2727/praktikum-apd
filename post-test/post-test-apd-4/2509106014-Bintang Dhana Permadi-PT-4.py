import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Selamat Datang di Bintang Store ===")

    member = input("Apakah Anda member? (y/n): ").lower()
    is_member = True if member == 'y' else False if member == 'n' else False
    login = False

    if is_member:
        kesempatan = 3
        while kesempatan > 0:
            print("\n=== Login Member ===")
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            if username == "" or password == "":
                print(" Username dan password tidak boleh kosong!")
            else:
                login = True if (username == "udin" and password == "1234") else False

                if login:
                    print(" Login berhasil!\n")
                    break
                else:
                    kesempatan -= 1
                    print(f" Login gagal! Sisa percobaan: {kesempatan}")

        if not login:
            print("\nAnda gagal login 3 kali, dianggap sebagai non-member.")
            is_member = False

    print("\n=== Menu Produk ===")
    print("1. Kaos Lacoste  - Rp250.000")
    print("2. Celana Rucas  - Rp400.000")
    print("3. Jaket H&M     - Rp550.000")
    print("4. Checkout")

    total = 0
    keranjang = ""
    while True:
        pilih = input("\nPilih produk (1-4): ")

        if pilih == "1":
            total += 250000
            keranjang += "Kaos Lacoste - Rp250.000\n"
            print(f" Kaos Lacoste ditambahkan! Total sementara: Rp{total:,}")
        elif pilih == "2":
            total += 400000
            keranjang += "Celana Rucas - Rp400.000\n"
            print(f" Celana Rucas ditambahkan! Total sementara: Rp{total:,}")
        elif pilih == "3":
            total += 550000
            keranjang += "Jaket H&M - Rp550.000\n"
            print(f" Jaket H&M ditambahkan! Total sementara: Rp{total:,}")
        elif pilih == "4":
            if total == 0:
                print("Keranjang kosong! Silakan belanja dulu.")
                continue
            else:
                break
        else:
            print(" Pilihan tidak valid!")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=== Struk Belanja ===")
    print(keranjang)
    print("------------------------------")

    if is_member and login:
        diskon = total * 0.15 
        total_setelah_diskon = total - diskon
        print(f"Total sebelum diskon : Rp{total:,}")
        print(f"Diskon (15%)         : Rp{diskon:,}")
        print(f"Total yang dibayar   : Rp{total_setelah_diskon:,}")
    else:
        print(f"Total yang dibayar   : Rp{total:,}")

    print("------------------------------")
    print("Terima kasih telah berbelanja di Bintang Store!\n")

    ulang = input("Apakah ingin melakukan transaksi lagi? (y/n): ").lower()
    if ulang != 'y':
        print("Program selesai. Sampai jumpa lagi!")
        break
