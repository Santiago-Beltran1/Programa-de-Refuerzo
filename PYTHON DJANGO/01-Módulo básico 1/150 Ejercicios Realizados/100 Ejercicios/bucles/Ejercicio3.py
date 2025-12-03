#Validar una contraseña con ciertos requisitos

while True:
    santiagoClave = input("Ingrese una contraseña (de mínimo 8 caracteres): ")
    if len(santiagoClave) >= 8:
        print("Contraseña aceptada")
        break
    else:
        print("Muy corta, intente de nuevo")
