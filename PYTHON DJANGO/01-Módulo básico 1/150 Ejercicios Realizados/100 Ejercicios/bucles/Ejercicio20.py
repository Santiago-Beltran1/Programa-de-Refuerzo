#Acceso de invitados a un evento

santiagoPermitidos = ["David", "Santiago", "Beltran"]

while True:
    santiagoNom = input("Nombre del invitado (o 'salir'): ")
    if santiagoNom == "salir":
        break
    if santiagoNom in santiagoPermitidos:
        print("Acceso permitido")
    else:
        print("Acceso denegado")
