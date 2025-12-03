#Verificación de usuario

santiagoUser = input("Ingrese su usuario: ")
santiagoPass = input("Ingrese su contraseña: ")

if santiagoUser == "admin" and santiagoPass == "1234":
    print("Acceso concedido")
else:
    print("Usuario o contraseña incorrectos")
