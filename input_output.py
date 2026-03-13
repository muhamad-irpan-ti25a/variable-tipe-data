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