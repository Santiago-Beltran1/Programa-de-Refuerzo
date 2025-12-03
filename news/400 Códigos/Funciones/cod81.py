def SantiagoBBuscarPalabra(SantiagoBTexto, SantiagoBPalabra):
    SantiagoPos = []
    SantiagoPa = SantiagoBTexto.split()
    for i, p in enumerate(SantiagoPa):
        if p.lower() == SantiagoBPalabra.lower():
            SantiagoPos.append(i+1)
    return SantiagoPos

SantiagoT = input("Texto: ")
SantiagoP = input("Palabra a buscar: ")
SantiagoPosi = SantiagoBBuscarPalabra(SantiagoT, SantiagoP)
print("Encontrada en posiciones:", SantiagoPosi if SantiagoPosi else "No encontrada.")
