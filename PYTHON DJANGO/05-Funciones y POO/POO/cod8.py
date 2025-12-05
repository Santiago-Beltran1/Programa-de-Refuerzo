class SantiagoBSV:
    def __init__(self, SantiagoNom):
        self.SantiagoNom = SantiagoNom
        self.SantiagoVivo = True

    def SantiagoResp(self):
        return f"{self.SantiagoNom} está respirando"


class SantiagoAnimal(SantiagoBSV):
    def __init__(self, SantiagoNom, SantiagoEspecie):
        super().__init__(SantiagoNom)
        self.SantiagoEsp = SantiagoEspecie

    def SantiagoMove(self):
        return f"{self.SantiagoNom} se está moviendo"


class SantiagoMamifero(SantiagoAnimal):
    def __init__(self, SantiagoNom, SantiagoEspecie, SantiagoTipoPelo):
        super().__init__(SantiagoNom, SantiagoEspecie)
        self.tipo_pelo = SantiagoTipoPelo

    def SantiagoCuid(self):
        return f"{self.SantiagoNom} está protegiendo a sus crías"


class SantiagoCaballo(SantiagoMamifero):
    def __init__(self, SantiagoNom, SantiagoRaza):
        super().__init__(SantiagoNom, "Canis familiaris", "corto")
        self.SantiagoRaza = SantiagoRaza

    def SantiagoSal(self):
        return f"{self.SantiagoNom} te saluda"


santiago1 = SantiagoCaballo("David", "Manzo")

print(santiago1.SantiagoResp())   
print(santiago1.SantiagoMove())    
print(santiago1.SantiagoCuid())  
print(santiago1.SantiagoSal())     
print(f"Raza: {santiago1.SantiagoRaza}")     