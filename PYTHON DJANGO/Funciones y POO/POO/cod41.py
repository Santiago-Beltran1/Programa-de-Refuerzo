class SantiagoB:
    def __init__(self, Santiago):
        self.__Santiago = Santiago

    def __SantiagoPriv(self):
        print(f"Privado: {self.__Santiago}")

    def SantiagoMos(self):
        self.__SantiagoPriv()

SantiagoObj = SantiagoB("Esta función es secreta")
SantiagoObj.SantiagoMos()
