#Sistema agregador de tareas

santiagoT = []
while True:
    santiagoTarea = input("Ingrese una tarea (o 'salir' para terminar): ")
    if santiagoTarea.lower() == "salir":
        break
    santiagoT.append(santiagoTarea)

print("Tareas pendientes:")
for t in santiagoT:
    print("-", t)
