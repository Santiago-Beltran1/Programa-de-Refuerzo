#Eliminador de contactos y actualizador de la agenda

santiagoNoms = ["Santiago", "Alejandro", "Ximena"]
santiagoPhones = ["1111", "2222", "3333"]

print("Agenda inicial:")
for i in range(len(santiagoNoms)):
    print(santiagoNoms[i], "->", santiagoPhones[i])

santiagoEli = input("Ingrese el contacto a eliminar: ")
if santiagoEli in santiagoNoms:
    santiagoPos = santiagoNoms.index(santiagoEli)
    santiagoNoms.pop(santiagoPos)
    santiagoPhones.pop(santiagoPos)
    print("Contacto eliminado. Agenda actualizada:", santiagoNoms)
else:
    print("Contacto no encontrado")
