def SantiagoPalindromo(SantiagoTexto):
    SantiagoTexto = SantiagoTexto.replace(" ", "").lower()
    return SantiagoTexto == SantiagoTexto[::-1]

def SantiagoMain():
    SantiagoTxt = input("Palabra o frase: ")
    print("Es palíndromo" if SantiagoPalindromo(SantiagoTxt) else "No es palíndromo")

SantiagoMain()
