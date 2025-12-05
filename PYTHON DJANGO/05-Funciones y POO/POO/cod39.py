class SantiagoBD:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoMos(self):
        print(f"Detalle: {self.Santiago}")

class Santiago:
    def __init__(self, Santiago, SantiagoDetalleObj):
        self.Santiago = Santiago
        self.SantiagoDetalleObj = SantiagoDetalleObj

    def SantiagoMos(self):
        print(f"Nombre: {self.Santiago}")
        self.SantiagoDetalleObj.SantiagoMos()

Santiago1 = SantiagoBD("Información extra")
SantiagoObj = Santiago("Santiago Principal", Santiago1)
SantiagoObj.SantiagoMos()
