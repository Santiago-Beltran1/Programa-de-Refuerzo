class SantiagoProd:
    def __init__(self, SantiagoNom, SantiagoCosto, SantiagoCant):
        self.SantiagoNom = SantiagoNom
        self.SantiagoCosto = SantiagoCosto
        self.SantiagoCant = SantiagoCant

    def SantiagoTot(self):
        return self.SantiagoCosto * self.SantiagoCant

Santiago1 = SantiagoProd("Cómic", 25000, 11)
print(f"EL costo del producto con todas sus unidades si se venden es de: ${Santiago1.SantiagoTot()}")
