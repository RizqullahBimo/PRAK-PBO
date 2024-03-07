import random

class Game:

    def __init__(self):
        self.__letter = random.choice('abcdefghijklmnopqrstuvwxyz')
        self.__tries = 0
        print("Selamat datang di game tebak huruf!")
        print("Saya telah memilih sebuah huruf acak dari a sampai z.")
        print("Anda memiliki 10 kesempatan untuk menebaknya.")

    def __del__(self):
        print("Terima kasih telah bermain game tebak huruf!")

    def limit_tries(func):
        def wrapper(self, *args):
            if self.__tries < 10:
                return func(self, *args)
            else:
                print("Anda telah kehabisan kesempatan. Anda kalah.")
                print(f"Huruf yang saya pilih adalah '{self.__letter}'.")
        return wrapper

    def start(self):
        while True:
            guess = input("Masukkan tebakan Anda: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Input tidak valid. Masukkan satu huruf.")
                continue

            self.check(guess)
            if self.__tries == 10 or guess == self.__letter:
                break

    @limit_tries
    def check(self, guess):
        self.__tries += 1
        if guess == self.__letter:
            print(f"Selamat! Anda menebak dengan benar dalam {self.__tries} kali.")
            print("Anda menang!")
        elif guess < self.__letter:
            print("Huruf Anda terlalu awal dalam abjad.")
            print(f"Anda masih memiliki {10 - self.__tries} kesempatan.")
        else:
            print("Huruf Anda terlalu akhir dalam abjad.")
            print(f"Anda masih memiliki {10 - self.__tries} kesempatan.")

game = Game()

game.start()

del game
