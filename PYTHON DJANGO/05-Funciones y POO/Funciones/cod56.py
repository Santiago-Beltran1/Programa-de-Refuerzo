def SantiagoLongitudPromedio(SantiagoTexto):
    SantiagoPalabras = SantiagoTexto.split()
    return sum(len(p) for p in SantiagoPalabras) / len(SantiagoPalabras)

def SantiagoMain():
    SantiagoTxt = input("Escribe una frase: ")
    print(f"Promedio de longitud de palabras: {SantiagoLongitudPromedio(SantiagoTxt):.2f}")

SantiagoMain()
