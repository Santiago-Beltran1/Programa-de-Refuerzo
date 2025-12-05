def SantiagoGuardarTexto(SantiagoTexto):
    with open("SantiagoArchivo.txt", "w", encoding="utf-8") as SantiagoB:
        SantiagoB.write(SantiagoTexto)
    print("Texto guardado correctamente en SantiagoArchivo.txt")

def SantiagoMain():
    SantiagoTxt = input("Escribe algo para guardar en un archivo: ")
    SantiagoGuardarTexto(SantiagoTxt)

SantiagoMain()
