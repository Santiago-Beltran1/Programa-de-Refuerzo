class SantiagoB:
    def __init__(self, SantiagoNom, SantiagoEdad):
        self.SantiagoNom = SantiagoNom
        self.SantiagoEdad = SantiagoEdad
        self.SantiagoVivo = True

    def SantiagoC(self):
        return f"{self.SantiagoNom} está comiendo"

    def SantiagoDorm(self):
        return f"{self.SantiagoNom} está durmiendo"

    def SantiagoSon(self):
        return "El animal hace un sonido"


class Santiago1(SantiagoB):
    def __init__(self, SantiagoNom, SantiagoEdad, SantiagoRaza):
        super().__init__(SantiagoNom, SantiagoEdad)
        self.raza = SantiagoRaza

    def SantiagoSal(self):
        return "Este es un perro"

    def SantiagoSon(self):
        return self.SantiagoSal()

    def SantiagoC(self):
        return f"{self.SantiagoNom} está comiendo croquetas de {self.raza}"


class Santiago2(SantiagoB):
    def __init__(self, SantiagoNom, SantiagoEdad, SantiagoCol):
        super().__init__(SantiagoNom, SantiagoEdad)
        self.SantiagoCol = SantiagoCol

    def maullar(self):
        return "Este es un gato"

    def SantiagoSon(self):
        return self.maullar()

    def SantiagoC(self):
        return f"{self.SantiagoNom} el gato {self.SantiagoCol} está comiendo pescado"


santiagoP = Santiago1("David", 1, "Pastor")
santiagoG = Santiago2("Santiago", 5, "Azul Ruso")

print(santiagoP.SantiagoDorm())  
print(santiagoG.SantiagoDorm())   

print(santiagoP.SantiagoC())   
print(santiagoG.SantiagoC())    

print(santiagoP.SantiagoSal())  
print(santiagoG.maullar())  
