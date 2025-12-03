while True:
    SantiagoB = input("Ingrese una contraseña: ")
    if len(SantiagoB) < 7:
        print("Debe tener al menos 7 caracteres.")
    elif not any(c.isdigit() for c in SantiagoB):
        print("Debe contener al menos un número.")
    elif not any(c.isupper() for c in SantiagoB):
        print("Debe contener al menos una letra mayúscula.")
    else:
        print("Contraseña válida.")
        break
