#Combinador de nombres con sus respectivos apellidos

santiagoNoms = ()
santiagoApellidos = ()

for i in range(2):
    santiagoNoms += (input(f"Ingrese el nombre {i+1}: "),)
    santiagoApellidos += (input(f"Ingrese el apellido {i+1}: "),)

print("Nombres completos:")
for i in range(len(santiagoNoms)):
    print(santiagoNoms[i] + " " + santiagoApellidos[i])
