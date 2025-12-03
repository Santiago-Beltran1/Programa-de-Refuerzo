#Reconocedor de contraseña

santiagoPass = "santiago1234"

while True:
    santiagoInt = input("Ingrese la contraseña: ")
    if santiagoInt == santiagoPass:
        print("Acceso concedido")
        break
    else:
        print("Contraseña incorrecta")
