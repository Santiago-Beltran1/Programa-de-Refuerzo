def SantiagoCrearUsuario(SantiagoNombre, SantiagoApellido):
    return (SantiagoNombre[:3] + SantiagoApellido[:3]).lower()

def SantiagoUsuarioFinal():
    SantiagoNom = input("Nombre: ")
    SantiagoApelli = input("Apellido: ")
    print("Tu nombre de usuario es:", SantiagoCrearUsuario(SantiagoNom, SantiagoApelli))

SantiagoUsuarioFinal()
