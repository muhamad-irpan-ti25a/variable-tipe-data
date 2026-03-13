name = input("isikan nama anda :")

#menggabungkan string dengan variabel

print("nama :", name)
print("1", end ="")
print("2", end ="")
print("3")


#separator
print("Andi", "budi", "robi", sep="-")



#penjumlahan
num1 = input("isikan bilangan 1 :")
num2 = input("isikan bilangan 2 :")
result = int(num1) + int(num2)

print(num1, "+", num2, "=", result)
print("{} + {} = {}".format(num1, num2, result))

f_name = input("isikan nama awal :")
m_name = input("isikan nama tengah :")
l_name = input("isikan nama akhir :")

print("nama anda : {} {} {}".format(f_name, m_name, l_name))

#index
print("nama anda : {1} {0} {1}".format(f_name, m_name, l_name))

#keyword
print("nama anda : {depan} {tengah} {belakang}".format(depan = f_name, tengah = m_name, belakang = l_name))

#output string manipulation

kampus = input("isikan nama kampus anda :")

print("huruf pertama :", kampus[0])
print("huruf terakhir :", kampus[-1])
print("Kalimat pertama: ", kampus[0:4])
print("membalik kalimat :", kampus[::-1])
print("mengambil kalimat ke dua :", kampus[5:1])

#memisah kata

full_name = input("isikan nama lengkap :")
split_name = full_name.split(" ")
f_name = split_name[0]
m_name = split_name[1]
l_name = split_name[2]

#output mnggunakan f-string
print(f"nama pertama {f_name}")
print(f"nama tengah {m_name}")
print(f"nama akhir {l_name}")

nomor_plat = input("isikan nomor plat mobil anda :")

#find -> tidak ketemu -1, ketemu -> posisi atau urutan

cari_karakter = nomor_plat.find("B")
print(cari_karakter)

#cek email itu valid atau tidak
#punya @
#punya .
#posisi @ harus disebelah kiri dari tanda .

email = input("isikan email anda :")
posisi_at = email.find("@")
posisi_dot = email.find(".")

#operator ternary

result = "valid" if (posisi_at > -1 and posisi_dot > -1) and (posisi_at < posisi_dot) else "tidak valid"

print(result)