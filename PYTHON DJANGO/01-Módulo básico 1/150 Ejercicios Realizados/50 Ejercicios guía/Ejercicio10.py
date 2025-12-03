# Validador de contraseñas
santiagoCon = str(input("Ingrese su contraseña: ")) 
santiagoLong = 7 

print("Contraseña a validar:", santiagoCon)
print("Longitud de la contraseña:", len(santiagoCon))

if len(santiagoCon) >= santiagoLong:
    print("La contraseña tiene la longitud correcta")
if santiagoCon.islower(): 
    print("error ponga almenos un caracter de su contraseña en mayúscula para continuar")
else: 
    print("Su contraseña es válida, fin del proceso")