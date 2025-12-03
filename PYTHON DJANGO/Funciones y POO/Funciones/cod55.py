def SantiagoClasificarEdad(SantiagoEdad):
    if SantiagoEdad < 12:
        return "Niño"
    elif SantiagoEdad < 18:
        return "Adolescente"
    elif SantiagoEdad < 60:
        return "Adulto"
    else:
        return "Adulto mayor"

def SantiagoMain():
    try:
        SantiagoE = int(input("Ingresa edad: "))
        print("Clasificación:", SantiagoClasificarEdad(SantiagoE))
    except:
        print("Número inválido.")

SantiagoMain()
