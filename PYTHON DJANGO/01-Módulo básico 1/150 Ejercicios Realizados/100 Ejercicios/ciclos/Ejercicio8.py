#Validador de contraseñas

santiagoCons = input("Ingrese una contraseña: ")

if len(santiagoCons) < 8:
    print("La contraseña es demasiado corta (mínimo 8 caracteres).")
elif not any(c.isdigit() for c in santiagoCons):
    print("La contraseña debe incluir al menos un número.")
elif not any(c.isupper() for c in santiagoCons):
    print("La contraseña debe incluir al menos una letra mayúscula.")
elif not any(c.islower() for c in santiagoCons):
    print("La contraseña debe incluir al menos una letra minúscula.")
else:
    print("Contraseña válida.")
