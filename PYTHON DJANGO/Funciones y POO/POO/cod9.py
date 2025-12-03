class SantiagoPersona:
    def __init__(self, SantiagoNom, SantiagoEdad):
        self.santiago_nom = SantiagoNom
        self.santiago_edad = SantiagoEdad 

    def SantiagoSaludar(self):
        return f"Hola, mi nombre es {self.santiago_nom}."

    def SantiagoCumplir(self):
        self.santiago_edad += 1
        return f"¡Feliz cumpleaños, {self.santiago_nom}! Ahora tienes {self.santiago_edad} años."


santiago1 = SantiagoPersona("Santiago Beltran", 17)
print(santiago1.SantiagoSaludar())
print(santiago1.SantiagoCumplir())


santiago_persona2 = SantiagoPersona("David", 20)
print(santiago_persona2.SantiagoSaludar())
