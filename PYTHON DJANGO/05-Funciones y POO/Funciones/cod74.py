def SantiagoBTextoAAscii(SantiagoBTexto):
    for SantiagoBLetra in SantiagoBTexto:
        print(f"{SantiagoBLetra} -> {ord(SantiagoBLetra)}")

SantiagoBTexto = input("Escribe un texto: ")
SantiagoBTextoAAscii(SantiagoBTexto)
