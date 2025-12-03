class SantiagoBProd:
    def __init__(self, SantiagoNom, SantiagoPrecio):
        self.SantiagoNom = SantiagoNom
        self.SantiagoPrecio = SantiagoPrecio

class SantiagoCarrito:
    def __init__(self):
        self.SantiagoItems = []

    def SantiagoAg(self, SantiagoProducto):
        self.SantiagoItems.append(SantiagoProducto)

    def SantiagoTot(self):
        return sum(item.SantiagoPrecio for item in self.SantiagoItems)

SantiagoProd1 = SantiagoBProd("Pasta", 3500)
SantiagoProd2 = SantiagoBProd("Frutiño", 1000)
SantiagoCar = SantiagoCarrito()
SantiagoCar.SantiagoAg(SantiagoProd1)
SantiagoCar.SantiagoAg(SantiagoProd2)
print(f"Total carrito: {SantiagoCar.SantiagoTot()}")
