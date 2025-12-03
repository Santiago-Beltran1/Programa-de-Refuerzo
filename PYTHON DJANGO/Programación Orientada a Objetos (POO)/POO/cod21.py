class SantiagoBVeh:
    def acelerar(self):
        raise NotImplementedError("Las subclases deben implementar 'acelerar()'")

class SantiagoBarco(SantiagoBVeh):
    def acelerar(self):
        return "El barco enciende su motor y navega velozmente por el agua."

class SantiagoTren(SantiagoBVeh):
    def acelerar(self):
        return "El tren silba y toma velocidad sobre los rieles."

class SantiagoMoto(SantiagoBVeh):
    def acelerar(self):
        return "La motocicleta ruge y acelera con potencia."

def SantiagoAce(vehiculo):
    print(f"Resultado de acelerar: {vehiculo.acelerar()}")

Santiago1 = SantiagoBarco()
Santiago2 = SantiagoTren()
Santiago3 = SantiagoMoto()

SantiagoAce(Santiago1)
SantiagoAce(Santiago2)
SantiagoAce(Santiago3)

SantiagoPkng = [SantiagoBarco(), SantiagoTren(), SantiagoMoto(), SantiagoTren()]
print("\nProbando la aceleración de todos los vehículos del parque:")
for v in SantiagoPkng:
    SantiagoAce(v)
