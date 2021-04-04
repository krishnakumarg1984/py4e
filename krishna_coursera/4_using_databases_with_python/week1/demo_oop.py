class PartyAnimal:
    x = 0

    def __init__(self):
        print("I am considered")

    def party(self):
        self.x += 1
        print("So far x", self.x)

    def __del__(self):
        print("I am destructed", self.x)


an = PartyAnimal()

# print("Type", type(an))
# print("Dir", dir(an))

an.party()
an.party()
an = 42
print("an contains", an)
