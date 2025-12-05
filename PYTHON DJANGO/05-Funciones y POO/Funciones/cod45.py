def SantiagoInvertir(SantiagoTexto):
    return SantiagoTexto[::-1]

def SantiagoMain():
    SantiagoTxt = input("Texto a invertir: ")
    print("Texto invertido:", SantiagoInvertir(SantiagoTxt))

SantiagoMain()
