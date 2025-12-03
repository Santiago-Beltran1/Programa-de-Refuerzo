def SantiagoConsonantes(SantiagoTexto):
    SantiagoTexto = SantiagoTexto.lower()
    return sum(1 for c in SantiagoTexto if c in "bcdfghjklmnpqrstvwxyz")

def SantiagoMain():
    SantiagoTxt = input("Escribe una frase: ")
    print(f"Número de consonantes: {SantiagoConsonantes(SantiagoTxt)}")

SantiagoMain()
