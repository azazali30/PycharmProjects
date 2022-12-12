class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("run", self.name)


player1 = PlayerCharacter("Md Azaz Ali")
player2 = PlayerCharacter("Sumit")
print(player1.name)
print(player2.name)