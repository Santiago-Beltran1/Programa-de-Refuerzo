class SantiagoB:
    SantiagoCont = 0

    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoSal(self):
        SantiagoB.SantiagoCont += 1
        print(f"Hola {self.Santiago}")

SantiagoObj = SantiagoB("Se esta llamando a la función")
SantiagoObj.SantiagoSal()
SantiagoObj.SantiagoSal()
print(f"La cantidad de saludos realizados obtenidos son: {SantiagoB.SantiagoCont}")
