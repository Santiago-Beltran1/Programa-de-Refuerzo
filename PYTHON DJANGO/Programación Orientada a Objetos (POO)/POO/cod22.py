class SantiagoB:
    def __init__(self, SantiagoNom, SantiagoEdad):
        self.__SantiagoNom = SantiagoNom
        self.__SantiagoEdad = SantiagoEdad

    @property
    def SantiagoEdad(self):
        return self.__SantiagoEdad

    @SantiagoEdad.setter
    def SantiagoEdad(self, nueva_edad):
        if 0 <= nueva_edad <= 150:
            self.__SantiagoEdad = nueva_edad
        else:
            raise ValueError("Edad inválida. Debe estar entre 0 y 150")

    @property
    def SantiagoNom(self):
        return self.__SantiagoNom

    @property
    def SantiagoMay(self):
        return self.__SantiagoEdad >= 18


Santiago1 = SantiagoB("David Santiago Beltran Pedraza", 17)

print(Santiago1.SantiagoEdad)        
Santiago1.SantiagoEdad = 26           
print(Santiago1.SantiagoEdad)         
print(Santiago1.SantiagoMay) 
