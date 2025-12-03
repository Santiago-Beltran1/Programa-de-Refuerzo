class SantiagoBProd:
    def __init__(self, SantiagoNom, SantiagoCosto, SantiagoStock):
        self.SantiagoNom = SantiagoNom
        self.SantiagoCosto = SantiagoCosto
        self.SantiagoStock = SantiagoStock

    def SantiagoInf(self):
        return f"Producto: {self.SantiagoNom}, Precio: {self.SantiagoCosto:.2f}, Stock: {self.SantiagoStock} unidades."

    def SantiagoActu(self, SantiagoCantidad):
        self.SantiagoStock += SantiagoCantidad
        return f"Stock actualizado. Nuevo stock de {self.SantiagoNom}: {self.SantiagoStock} unidades."

    def SantiagoTot(self, SantiagoUnidades):
        if SantiagoUnidades > 0 and SantiagoUnidades <= self.SantiagoStock:
            return f"El valor total de {SantiagoUnidades} unidades de {self.SantiagoNom} es {SantiagoUnidades * self.SantiagoCosto:.2f}."
        elif SantiagoUnidades > self.SantiagoStock:
            return "Stock insuficiente."
        else:
            return "La cantidad debe ser positiva."

SantiagoP1 = SantiagoBProd("Sofá Cama", 1200000, 20)
print(SantiagoP1.SantiagoInf())
print(SantiagoP1.SantiagoActu(11))
print(SantiagoP1.SantiagoInf())
print(SantiagoP1.SantiagoTot(2))
print(SantiagoP1.SantiagoTot(3))
print(SantiagoP1.SantiagoActu(-10))
print(SantiagoP1.SantiagoInf())
print(SantiagoP1.SantiagoTot(5))
