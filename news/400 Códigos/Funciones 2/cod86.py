class SantiagoC:
    def __init__(self):
        self.SantiagoItems = []

    def SantiagoAg(self, SantiagoNom, SantiagoCosto, SantiagoCant):
        self.SantiagoItems.append({"nombre":SantiagoNom,"precio":SantiagoCosto,"cantidad":SantiagoCant})
        print(f"Item agregado: {SantiagoNom} x{SantiagoCant} a ${SantiagoCosto} cada uno")

    def SantiagoTot(self):
        SantiagoTotal = sum(item["precio"]*item["cantidad"] for item in self.SantiagoItems)
        print(f"SantiagoTotal del carrito: ${SantiagoTotal}")

SantiagoMiCarrito = SantiagoC()
SantiagoMiCarrito.SantiagoAg("Lapiz", 3, 2000)
SantiagoMiCarrito.SantiagoAg("Cuaderno", 5, 5000)
SantiagoMiCarrito.SantiagoTot()
