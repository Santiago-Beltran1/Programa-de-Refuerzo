# Tupla para almacenar nombres sin repetir

santiagoNoms = ()

for i in range(3):
    santiagoNom = input("Ingrese un nombre: ")
    if santiagoNom not in santiagoNoms:
        santiagoNoms += (santiagoNom,)
    else:
        print("Ese nombre ya fue ingresado")

print("Nombres finales:", santiagoNoms)
