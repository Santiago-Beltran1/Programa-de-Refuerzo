class SantiagoBEst:
    SantiagoIns = "SENA Mosquera - CBA"

    def __init__(self, SantiagoNom, SantiagoEdad, SantiagoCurso):
        self.SantiagoNom = SantiagoNom
        self.SantiagoEdad = SantiagoEdad
        self.SantiagoCurso = SantiagoCurso
        self.SantiagoPunts = []

        # Atributo privado
        self.__SantiagoPromI = 0.0

    def SantiagoAg(self, SantiagoPunt):
        self.SantiagoPunts.append(SantiagoPunt)
        self.__SantiagoCalcP()

    def __SantiagoCalcP(self):
        if self.SantiagoPunts:
            self.__SantiagoPromI = sum(self.SantiagoPunts) / len(self.SantiagoPunts)

    def SantiagoProm(self):
        return self.__SantiagoPromI


# Uso
Santiago1 = SantiagoBEst("Santiago", 17, "ADSO")
Santiago2 = SantiagoBEst("Beltran", 17, "Comercio")

print(Santiago1.SantiagoIns)  
print(Santiago2.SantiagoIns)

Santiago1.SantiagoAg(3.1)
Santiago1.SantiagoAg(4.0)

Santiago2.SantiagoAg(5.0)
Santiago2.SantiagoAg(1.2)

print(f"Promedio de {Santiago1.SantiagoNom}: {Santiago1.SantiagoProm()}")
print(f"Promedio de {Santiago2.SantiagoNom}: {Santiago2.SantiagoProm()}")
