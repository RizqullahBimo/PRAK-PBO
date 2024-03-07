class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def method1(self):
        # Contoh method 1
        return f"{self.__nama} memiliki NIM {self.__nim}"

    def method2(self, tahun):
        # Contoh method 2
        return f"{self.__nama} akan lulus pada tahun {tahun}"

    def method3(self, status):
        # Contoh method 3
        if status:
            return f"{self.__nama} adalah mahasiswa"
        else:
            return f"{self.__nama} bukan mahasiswa"


# Object pertama
mahasiswa1 = Mahasiswa("122140220", "Rizqullah Bimo", 2026)

# Object kedua
mahasiswa2 = Mahasiswa("13109890", "Cristiano Ronaldo", 2022, isMahasiswa=True)

# Print nama dan nim mahasiswa
print(f"Nama dan NIM Mahasiswa 1: {mahasiswa1.get_nama()} - {mahasiswa1.get_nim()}")
print(f"Nama dan NIM Mahasiswa 2: {mahasiswa2.get_nama()} - {mahasiswa2.get_nim()}")

# Print nama mahasiswa dan tahun lulus
print(f"Nama Mahasiswa 1 dan Tahun Lulus: {mahasiswa1.get_nama()} - {mahasiswa1.method2(2026)}")
print(f"Nama Mahasiswa 2 dan Tahun Lulus: {mahasiswa2.get_nama()} - Tidak akan lulus")

# Print status mahasiswa
print(f"Status Mahasiswa 1: {mahasiswa1.method3(mahasiswa1.isMahasiswa)}")
print(f"Status Mahasiswa 2: {mahasiswa2.method3(not mahasiswa2.isMahasiswa)}")

