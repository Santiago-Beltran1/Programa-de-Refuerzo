#Buscador de elementos

santiagoCols = ("rojo", "azul", "verde", "amarillo")
santiagoBus = input("Color a buscar: ")

if santiagoBus in santiagoCols:
    print(f"{santiagoBus} está en la lista de colores")
else:
    print("No está en la lista")
