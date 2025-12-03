#Ingresarle un nuevo país a la marca 

santiagoMarcas = {"Toyota": "Japón", "BMW": "Alemania", "Ford": "EE.UU."}

print("Diccionario original:", santiagoMarcas)
santiagoMarca = input("¿Qué marca quieres modificar?: ")

if santiagoMarca in santiagoMarcas:
    santiagoOp = input(f"El valor actual de {santiagoMarca} es '{santiagoMarcas[santiagoMarca]}'. ¿Deseas cambiarlo? (si/no): ").lower()
    if santiagoOp == "si":
        santiagoNewValor = input(f"Ingresa el nuevo valor para {santiagoMarca}: ")
        santiagoMarcas[santiagoMarca] = santiagoNewValor
        print("Diccionario actualizado:", santiagoMarcas)
    else:
        print("No se realizaron cambios.")
else:
    print("La marca no existe en el diccionario.")
