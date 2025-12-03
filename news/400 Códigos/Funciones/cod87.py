def SantiagoBUsuarios():
    SantiagoBLista = []
    while True:
        print("\n1. Registrar usuario\n2. Buscar usuario\n3. Salir")
        SantiagoBOpcion = input("Opción: ")
        if SantiagoBOpcion == "1":
            SantiagoBNombre = input("Nombre: ")
            SantiagoBCorreo = input("Correo: ")
            SantiagoBLista.append({"nombre": SantiagoBNombre, "correo": SantiagoBCorreo})
        elif SantiagoBOpcion == "2":
            SantiagoBBuscar = input("Nombre a buscar: ")
            encontrados = [u for u in SantiagoBLista if SantiagoBBuscar.lower() in u["nombre"].lower()]
            print(encontrados if encontrados else "No encontrado")
        elif SantiagoBOpcion == "3":
            break

SantiagoBUsuarios()
