def SantiagoTareas():
    SantiagoLista = []
    while True:
        print("\n1. Agregar tarea\n2. Ver tareas\n3. Salir")
        SantiagoOpcion = input("Opción: ")
        if SantiagoOpcion == "1":
            SantiagoT = input("Escribe una tarea: ")
            SantiagoLista.append(SantiagoT)
        elif SantiagoOpcion == "2":
            for i, t in enumerate(SantiagoLista, 1):
                print(f"{i}. {t}")
        elif SantiagoOpcion == "3":
            break
        else:
            print("Opción inválida.")

SantiagoTareas()
