class SantiagoB:
    def __init__(self, SantiagoNom, SantiagoTip, SantiagoEdad):
        self.SantiagoNom = SantiagoNom
        self.SantiagoTip = SantiagoTip
        self.SantiagoEdad = SantiagoEdad

    def SantiagoSalu(self):
        return f"{self.SantiagoNom} te da la bienvenida"

    def SantiagoDesc(self):
        return f"{self.SantiagoNom} es un gato de especie {self.SantiagoTip} de {self.SantiagoEdad} año(s)."

# Uso de la clase
Santiago1 = SantiagoB("Santiago", "Azul Ruso", 1)
Santiago2 = SantiagoB("Beltran", "Esfinje", 2)

print(Santiago1.SantiagoSalu())
print(Santiago1.SantiagoDesc())
print(Santiago2.SantiagoSalu())
print(Santiago2.SantiagoDesc())
