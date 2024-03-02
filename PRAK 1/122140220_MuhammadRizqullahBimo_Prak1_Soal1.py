

limitBawah = int(input("Inputkan batas bawah : "))
limitAtas = int(input("Inputkan batas atas : "))
total = 0

if limitBawah < 0 or limitAtas < 0:
    print("Batas bawah dan atas tidak boleh dibawah nol")
else:
    for num in range(limitBawah, limitAtas):
        if num % 2 == 1:
            print(num)
            total += num
    print("Jumlah total bilangan ganjil adalah = " + str(total))
