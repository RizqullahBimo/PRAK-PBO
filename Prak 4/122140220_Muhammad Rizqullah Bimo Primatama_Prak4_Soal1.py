class Hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin

    def bersuara(self):
        print(f"{self.nama} bersuara: ")
        self.suara()

    def makan(self):
        print(f"{self.nama} sedang makan: tulang")

    def minum(self):
        print(f"{self.nama} sedang minum air")

    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        print("Meong!")

class Anjing(Hewan):
    def suara(self):
        print("Guk Guk!")

hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")

print(hewan1.nama)
print(hewan2.nama)

hewan1.bersuara()
hewan1.makan()

hewan2.bersuara()
hewan2.makan()