def SantiagoContarPalabras(SantiagoTexto):
    return len(SantiagoTexto.split())

def SantiagoMain():
    SantiagoTxt = input("Escribe un texto: ")
    print(f"Número de palabras: {SantiagoContarPalabras(SantiagoTxt)}")

SantiagoMain()
