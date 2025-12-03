from abc import ABC, abstractmethod

class SantiagoBebida(ABC):
    @abstractmethod
    def SantiagoCosto(self):
        pass

    @abstractmethod
    def SantiagoDesc(self):
        pass

class SantiagoJugo(SantiagoBebida):
    def SantiagoCosto(self):
        return 3.0

    def SantiagoDesc(self):
        return "Jugo natural"

class SantiagoDecora(SantiagoBebida, ABC):
    def __init__(self, bebida: SantiagoBebida):
        self._bebida = bebida

    @abstractmethod
    def SantiagoCosto(self):
        pass

    @abstractmethod
    def SantiagoDesc(self):
        pass

class SantiagoHielo(SantiagoDecora):
    def SantiagoCosto(self):
        return self._bebida.SantiagoCosto() + 0.3

    def SantiagoDesc(self):
        return self._bebida.SantiagoDesc() + ", con hielo"

class SantiagoMiel(SantiagoDecora):
    def SantiagoCosto(self):
        return self._bebida.SantiagoCosto() + 0.7

    def SantiagoDesc(self):
        return self._bebida.SantiagoDesc() + ", con miel"

class SantiagoFrutaExtra(SantiagoDecora):
    def SantiagoCosto(self):
        return self._bebida.SantiagoCosto() + 1.2

    def SantiagoDesc(self):
        return self._bebida.SantiagoDesc() + ", con fruta extra"

print("--- Patrón Decorator con prefijo Santiago ---")

Santiago1 = SantiagoJugo()
print(f"Pedido 1: {Santiago1.SantiagoDesc()} - Costo: {Santiago1.SantiagoCosto():.2f}€")

Santiago2 = SantiagoHielo(SantiagoJugo())
print(f"Pedido 2: {Santiago2.SantiagoDesc()} - Costo: {Santiago2.SantiagoCosto():.2f}€")

Santiago3 = SantiagoMiel(SantiagoHielo(SantiagoJugo()))
print(f"Pedido 3: {Santiago3.SantiagoDesc()} - Costo: {Santiago3.SantiagoCosto():.2f}€")

Santiago4 = SantiagoFrutaExtra(SantiagoMiel(SantiagoHielo(SantiagoJugo())))
print(f"Pedido 4: {Santiago4.SantiagoDesc()} - Costo: {Santiago4.SantiagoCosto():.2f}€")

Santiago5 = SantiagoFrutaExtra(SantiagoJugo())
print(f"Pedido 5: {Santiago5.SantiagoDesc()} - Costo: {Santiago5.SantiagoCosto():.2f}€")
