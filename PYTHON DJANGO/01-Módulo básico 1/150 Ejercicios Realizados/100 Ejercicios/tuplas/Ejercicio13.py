# Edades mínimas

santiagoRequires = (("Cine", 12), ("Licencia", 18))

santiagoActividad = input("Actividad (Cine/Licencia): ")
santiagoEdad = int(input("Ingrese su edad: "))

for santiagoAcr, req in santiagoRequires:
    if santiagoAcr.lower() == santiagoActividad.lower():
        if santiagoEdad >= req:
            print("Acceso permitido")
        else:
            print("Acceso denegado, necesitas", req, "años")
