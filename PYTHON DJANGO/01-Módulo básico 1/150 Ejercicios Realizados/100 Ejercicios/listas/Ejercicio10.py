#Ingreso y busqueda de contactos

santiagoContacts = ["David", "Santiago", "Beltran", "Pedraza"]
print("Contactos actuales:", santiagoContacts)

santiagoNew = input("Ingrese un nuevo contacto: ")
santiagoContacts.append(santiagoNew)
print("Lista actualizada:", santiagoContacts)

santiagoBus = input("¿Qué contacto desea buscar? ")
if santiagoBus in santiagoContacts:
    print(santiagoBus, "está en la lista en la posición", santiagoContacts.index(santiagoBus))
else:
    print("Contacto no encontrado")
