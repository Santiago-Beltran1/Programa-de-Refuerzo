# Tupla con contraseñas válidas

santiagoPass = ("admin123", "clave2024", "python456")

santiagoIngress = input("Ingrese su contraseña: ")
if santiagoIngress in santiagoPass:
    print("Acceso concedido")
else:
    print("Acceso denegado")
