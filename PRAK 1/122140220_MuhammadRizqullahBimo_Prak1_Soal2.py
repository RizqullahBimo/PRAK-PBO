

jarijari = int(input("jari-jari : "))
phi = 3.14

if jarijari < 0:
    print("jari-jari lingkaran tidak boleh negatif")
else:
    luas = phi * jarijari ** 2
    keliling = 2 * phi * jarijari

    print("Luas : ", luas)
    print("Keliling : ", keliling)
