class SantiagoBMaq:
    def SantiagoOpera(self):
        raise NotImplementedError("Las subclases deben implementar 'operar()'")

class SantiagoTractor(SantiagoBMaq):
    def SantiagoOpera(self):
        return "El tractor está arando el campo."

class SantiagoExcavadora(SantiagoBMaq):
    def SantiagoOpera(self):
        return "La excavadora está moviendo tierra."

class SantiagoGrúa(SantiagoBMaq):
    def SantiagoOpera(self):
        return "La grúa está levantando cargas pesadas."

def SantiagoVer(maquina):
    print(f"Operación en curso: {maquina.SantiagoOpera()}")

Santiago1 = SantiagoTractor()
Santiago2 = SantiagoExcavadora()
Santiago3 = SantiagoGrúa()

SantiagoVer(Santiago1)
SantiagoVer(Santiago2)
SantiagoVer(Santiago3)

SantiagoActivas = [SantiagoTractor(), SantiagoExcavadora(), SantiagoGrúa(), SantiagoTractor(), SantiagoGrúa()]
print("\nOperación de todas las máquinas activas:")
for SantiagoMaquina in SantiagoActivas:
    SantiagoVer(SantiagoMaquina)
