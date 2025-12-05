def SantiagoBFormatear(SantiagoBTexto):
    print("1. Mayúsculas")
    print("2. Minúsculas")
    print("3. Título")
    SantiagoBOpcion = input("Opción: ")
    if SantiagoBOpcion == "1":
        print(SantiagoBTexto.upper())
    elif SantiagoBOpcion == "2":
        print(SantiagoBTexto.lower())
    elif SantiagoBOpcion == "3":
        print(SantiagoBTexto.title())
    else:
        print("Opción inválida")

SantiagoBTexto = input("Ingrese texto: ")
SantiagoBFormatear(SantiagoBTexto)
