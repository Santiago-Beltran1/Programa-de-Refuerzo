from abc import ABC, abstractmethod

class SantiagoBElectro(ABC):
    @abstractmethod
    def SantiagoTipo(self):
        pass

    @abstractmethod
    def SantiagoEncender(self):
        pass

class SantiagoLavadora(SantiagoBElectro):
    def SantiagoTipo(self):
        return "Lavadora"

    def SantiagoEncender(self):
        return "La lavadora Santiago empieza a lavar la ropa."

class SantiagoMicroondas(SantiagoBElectro):
    def SantiagoTipo(self):
        return "Microondas"

    def SantiagoEncender(self):
        return "El microondas Santiago calienta la comida rápidamente."

class SantiagoRefrigerador(SantiagoBElectro):
    def SantiagoTipo(self):
        return "Refrigerador"

    def SantiagoEncender(self):
        return "El refrigerador Santiago mantiene los alimentos frescos."

class SantiagoFabricaElectro(ABC):
    @abstractmethod
    def SantiagoCrear(self):
        pass

    def SantiagoOperar(self):
        aparato = self.SantiagoCrear()
        return f"Creando {aparato.SantiagoTipo()} y luego... {aparato.SantiagoEncender()}"

class SantiagoFabricaLavad(SantiagoFabricaElectro):
    def SantiagoCrear(self):
        return SantiagoLavadora()

class SantiagoFabricaMicroo(SantiagoFabricaElectro):
    def SantiagoCrear(self):
        return SantiagoMicroondas()

class SantiagoFabricaRefri(SantiagoFabricaElectro):
    def SantiagoCrear(self):
        return SantiagoRefrigerador()

def SantiagoCliente(fabrica: SantiagoFabricaElectro):
    print(f"Cliente: He pedido un electrodoméstico y: {fabrica.SantiagoOperar()}")

print("--- Patrón Factory Method con prefijo Santiago ---")

print("\nSolicitando una lavadora:")
SantiagoCliente(SantiagoFabricaLavad())

print("\nSolicitando un microondas:")
SantiagoCliente(SantiagoFabricaMicroo())

print("\nSolicitando un refrigerador:")
SantiagoCliente(SantiagoFabricaRefri())
