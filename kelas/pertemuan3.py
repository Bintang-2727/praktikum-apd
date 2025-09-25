# nilai = 70

# if nilai > 75:
#     print('Nilai A')

# # input nilai
# umur = int(input("Masukkan umur Anda: "))
# # misalnya, umur = 16
# # Percabangan
# if umur < 13:
#     kategori = "Anak-anak"
# elif umur < 18:
#     kategori = "Remaja"
# elif umur < 60:
#     kategori = "Dewasa"
# else:
#     kategori = "Lansia"
# # Menampilkan umur dan kategori
# print("Umur:", umur, "Kategori:", kategori)

# tinggi = int(input("Masukkan tinggi badan Anda (cm): "))

# if tinggi >= 145:
#     print("Anda boleh menaiki wahana Roller Coaster Tornado 🎢")
# else:
#     print("Maaf, Anda tidak boleh menaiki wahana Roller Coaster Tornado 😔")

total_belanja = int(input("Masukkan total belanja Anda (Rp): "))

if total_belanja > 100000:
    diskon = 0.50
    print("Anda mendapat diskon 50%")
elif total_belanja > 50000:
    diskon = 0.30
    print("Anda mendapat diskon 30%")
else:
    diskon = 0
    print("Maaf, Anda tidak mendapat diskon")

# Hitung total yang harus dibayar
potongan = total_belanja * diskon
total_bayar = total_belanja - potongan

print(f"Total belanja : Rp{total_belanja:,}")
print(f"Potongan      : Rp{potongan:,}")
print(f"Total bayar   : Rp{total_bayar:,}")
