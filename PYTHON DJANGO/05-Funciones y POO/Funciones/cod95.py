def SantiagoNormalizar(SantiagoNombre):
    return SantiagoNombre.strip().capitalize()

def SantiagoCompararNombres(SantiagoN1, SantiagoN2):
    return SantiagoNormalizar(SantiagoN1) == SantiagoNormalizar(SantiagoN2)

def SantiagoVerificarNombres():
    SantiagoN1 = input("Primer nombre: ")
    SantiagoN2 = input("Segundo nombre: ")
    if SantiagoCompararNombres(SantiagoN1, SantiagoN2):
        print("Son el mismo nombre")
    else:
        print("Son diferentes")

SantiagoVerificarNombres()
