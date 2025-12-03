class SantiagoB:
    def __init__(self):
        self.Santiago = {}

    def agregarSantiago(self, SantiagoClave, SantiagoValor):
        self.Santiago[SantiagoClave] = SantiagoValor

    def SantiagoMos(self):
        print("Diccionario Santiago:", self.Santiago)

SantiagoObj = SantiagoB()
SantiagoObj.agregarSantiago("Edad", 17)
SantiagoObj.agregarSantiago("Ciudad", "Mosquera")
SantiagoObj.SantiagoMos()
