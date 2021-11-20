class VideoGame:
    def viata(self):
        self.HP = 0

    def stamina(self):
        self.energy = 0

    def attack(self):
        self.DMG = 0

    def getstats(self):
        print(self.name)
        print(f"HP: {self.HP}")
        print(f"STAMINA: {self.stamina()}")
        print(f"DMG: {self.DMG}")
        print()


if __name__ == "__main__":
    Urs = VideoGame("Urs")
    Urs.viata(250)
    Urs.stamina(40)
    Urs.attack(40)

    Lup = VideoGame("Lup")
    Lup.viata(100)
    Lup.stamina(100)
    Lup.attack(75)

    Urs.getstats()
    Lup.getstats()

while Urs.viata >= 0 and Lup.viata >= 0:
    Urs.viata = Urs.viata - Lup.DMG
    Lup.viata = Lup.viata - Urs.DMG

if Urs.viata <= 0 and Lup.viata <= 0:
    print("Egalitate")
elif Urs.viata <= 0:
    print("Ursul a castigat")
elif Lup.viata <= 0:
    print("Lupul a castigat")

