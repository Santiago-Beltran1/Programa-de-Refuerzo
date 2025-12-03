def SantiagoBGenerarUsuario(SantiagoBNombre, SantiagoBApellido):
    SantiagoUser = (SantiagoBNombre[:3] + SantiagoBApellido[-3:] + "123").lower()
    print("Tu nombre de usuario sugerido es:", SantiagoUser)

SantiagoBNombre = input("Nombre: ")
SantiagoBApellido = input("Apellido: ")
SantiagoBGenerarUsuario(SantiagoBNombre, SantiagoBApellido)
