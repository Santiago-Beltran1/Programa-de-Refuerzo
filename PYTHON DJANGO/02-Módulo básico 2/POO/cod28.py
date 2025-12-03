class SantiagoB:
    def SantiagoEstado(self):
        raise NotImplementedError("Las subclases deben implementar 'SantiagoEstado()'")

class SantiagoAtlas(SantiagoB):
    def __init__(self, modelo):
        self.modelo = modelo
        self.bateria = 100
        self.integridad = 100

    def SantiagoEstado(self):
        return f"El robot Atlas modelo {self.modelo} está activo. Batería: {self.bateria}, Integridad: {self.integridad}"

class SantiagoBeta(SantiagoB):
    def __init__(self, modelo):
        self.modelo = modelo
        self.bateria = 80
        self.integridad = 90

    def SantiagoEstado(self):
        return f"El robot Beta modelo {self.modelo} está activo. Batería: {self.bateria}, Integridad: {self.integridad}"

def SantiagoVer(robot):
    print(robot.SantiagoEstado())

SantiagoR1 = SantiagoAtlas("XJ-9")
SantiagoR2 = SantiagoBeta("K-2")

SantiagoVer(SantiagoR1)
SantiagoVer(SantiagoR2)

SantiagoActivos = [SantiagoAtlas("XJ-9"), SantiagoBeta("K-2"), SantiagoAtlas("XJ-8")]
print("\nEstado de todos los robots activos:")
for r in SantiagoActivos:
    SantiagoVer(r)
