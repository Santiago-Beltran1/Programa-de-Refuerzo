def SantiagoBAnalizarTexto(SantiagoBTexto):
    SantiagoBLetras = sum(c.isalpha() for c in SantiagoBTexto)
    SantiagoBNumeros = sum(c.isdigit() for c in SantiagoBTexto)
    SantiagoBSignos = len(SantiagoBTexto) - SantiagoBLetras - SantiagoBNumeros
    print(f"Letras: {SantiagoBLetras}, Números: {SantiagoBNumeros}, Signos: {SantiagoBSignos}")

SantiagoBTexto = input("Ingrese texto para analizar: ")
SantiagoBAnalizarTexto(SantiagoBTexto)
