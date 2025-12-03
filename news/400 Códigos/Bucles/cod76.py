SantiagoB = {}

while True:
    print("\n1. Registrar estudiante")
    print("2. Buscar estudiante")
    print("3. Salir")
    SantiagoOpc = input("Opción: ")

    if SantiagoOpc == "1":
        SantiagoNom = input("Nombre: ")
        SantiagoEdad = int(input("Edad: "))
        SantiagoB[SantiagoNom] = SantiagoEdad
    elif SantiagoOpc == "2":
        SantiagoBus = input("Nombre a buscar: ")
        if SantiagoBus in SantiagoB:
            print(f"{SantiagoBus} tiene {SantiagoB[SantiagoBus]} años.")
        else:
            print("No encontrado.")
    elif SantiagoOpc == "3":
        break
    else:
        print("Opción inválida.")
