nama = input("Masukkan Nama Pasien : ")
tinggi = float(input("Masukkan Tinggi Badan (cm) : "))
berat = float(input("Masukkan Berat Badan (kg) : "))

beratIdeal = tinggi - 100
isKelebihan = berat > beratIdeal

statusList = ["Berat Badan Ideal", "Berat Badan Kelebihan"]
status = statusList[int(isKelebihan)]

print("-" * 81)
print("|{:^79}|".format(f"HASIL CEK BERAT BADAN {nama}"))
print("-" * 81)

print("-" * 81)
print(f"| Nama Pasien       : {nama:<58}|")
print(f"| Tinggi Badan      : {tinggi:.0f} cm{'':<52}|")
print(f"| Berat Badan       : {berat:.0f} kg{'':<53}|")
print(f"| Berat Ideal       : {beratIdeal:.0f} kg{'':<53}|")
print(f"| Status            : {status:<58}|")
print("-" * 81)