SantiagoB = []
while True:
    SantiagoMsg = input("Escriba un mensaje ('salir' para terminar): ")
    if SantiagoMsg.lower() == "salir":
        break
    SantiagoB.append(SantiagoMsg)

print("Mensajes guardados:")
for SantiagoM in SantiagoB:
    print("-", SantiagoM)
