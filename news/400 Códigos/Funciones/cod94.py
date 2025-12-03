def SantiagoEsMayor(SantiagoEdad):
    return SantiagoEdad >= 18

def SantiagoCategoriaEdad(SantiagoEdad):
    if SantiagoEdad < 13:
        return "Niño"
    elif SantiagoEdad < 18:
        return "Adolescente"
    else:
        return "Adulto"

def SantiagoVerificadorEdad():
    SantiagoEdad = int(input("Ingresa tu edad: "))
    print("Eres mayor de edad:", SantiagoEsMayor(SantiagoEdad))
    print("Categoría:", SantiagoCategoriaEdad(SantiagoEdad))

SantiagoVerificadorEdad()
