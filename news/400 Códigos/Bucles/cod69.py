SantiagoB = "santiago"
SantiagoC = "1234"
SantiagoInt = 0

while SantiagoInt < 3:
    SantiagoInUsuario = input("Usuario: ")
    SantiagoInClave = input("Contraseña: ")
    if SantiagoInUsuario == SantiagoB and SantiagoInClave == SantiagoC:
        print("Inicio de sesión exitoso.")
        break
    else:
        SantiagoInt += 1
        print("Datos incorrectos. Intento", SantiagoInt)
else:
    print("Acceso denegado por demasiados intentos.")
