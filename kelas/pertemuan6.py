# Membuat set
#buah = {"apel", "jeruk", "mangga", "apel"}
#print(buah)
#for i in buah:
    #print(i, end=' ')


# angka = {1,2,3,4,5}

# unik = set(angka)
# print(unik)

# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }

# print(Daftar_buku["Buku1"])

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {
# "Instagram" : "@anandadaffah",
# "Twitter" : "@anandadaffah"
# }
# }
# print(Biodata)
# for i, j in Biodata.items():
#     print(i)
#     print(j)

# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get('nama')}")
# print(Biodata.get("Nama"))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# print(Film)

# Film["Zombieland"] = "Comedy"
# Film.update({"upin-ipin" : "Thriller"})
# #Setelah Ditambah

# del Film['The Conjuring']

# # print(Film)

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['The Chainsmoker'][0])

# a ={10,11,12}
# b ={11,13,14}

# c = a | b

# print(c)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}

print("Nilai : ", Nilai.setdefault("Kimia", 70))