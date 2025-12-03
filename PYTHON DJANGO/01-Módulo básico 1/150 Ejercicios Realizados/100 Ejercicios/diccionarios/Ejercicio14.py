#Simulador de una agenda

santiagoAgenda = {"David": "3001111111", "Santiago": "3022222222"}
print("Agenda:", santiagoAgenda)

santiagoAccion = input("¿Deseas agregar, eliminar o ver un contacto? ").lower()

if santiagoAccion == "agregar":
    santiagoNom = input("Nombre: ")
    santiagoTel = input("Teléfono: ")
    santiagoAgenda[santiagoNom] = santiagoTel
elif santiagoAccion == "eliminar":
    santiagoNom = input("Nombre a eliminar: ")
    santiagoAgenda.pop(santiagoNom, None)
elif santiagoAccion == "ver":
    for santiagoNom, santiagoTel in santiagoAgenda.items():
        print(f"{santiagoNom}: {santiagoTel}")

print("Agenda final:", santiagoAgenda)
