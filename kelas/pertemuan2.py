# print('Hello wprld')
# namaDepan = 'bintang'
# namaBelakang = 'dhana permadi'
# print(namaDepan+namaBelakang)
# teks = 'saya suka belajar apd'
# print(teks[5:9])

# prodi = ['Informatika','Sistem Informasi','Arsitek']
# print(prodi[0])

# nama = input('Masukan Nama Kalian : ')
# print("Hallo nama saya",nama)

print("===Program Login Sederhana ===")

username_benar = "admin"
password_benar = "1234"

while True:  # perulangan tak terbatas
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == "" or password == "":
        print("Username dan password tidak boleh kosong!")
        continue  # kembali ke loop untuk memasukkan ulang
    
    if username == username_benar and password == password_benar:
        print("Login berhasil, selamat datang,", username + "!")
        break  # keluar dari loop jika benar
    