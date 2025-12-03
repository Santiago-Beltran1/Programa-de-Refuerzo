#Visualizador de elementos ingresados inversamente

santiagoE = []

while True:
    print("\n1. Agregar elemento")
    print("2. Ver lista original")
    print("3. Ver lista al revés")
    print("4. Salir")
    santiagoOp = input("Opción: ")

    if santiagoOp == "1":
        santiagoElem = input("Elemento: ")
        santiagoE.append(santiagoElem)
    elif santiagoOp == "2":
        print("Lista original:", santiagoE)
    elif santiagoOp == "3":
        copia = santiagoE.copy()
        copia.reverse()
        print("Lista al revés:", copia)
    elif santiagoOp == "4":
        break
