def SantiagoBContarLetra(SantiagoTexto, SantiagoLetra):
    return SantiagoTexto.lower().count(SantiagoLetra.lower())

SantiagoText = input("Texto: ")
SantiagoL = input("Letra a contar: ")
print(f"La letra '{SantiagoL}' aparece {SantiagoBContarLetra(SantiagoText, SantiagoL)} veces.")
