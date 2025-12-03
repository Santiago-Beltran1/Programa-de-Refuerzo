def SantiagoBTareas():
    SantiagoBLista = []
    for i in range(3):
        SantiagoBTarea = input("Nombre de tarea: ")
        SantiagoBImportancia = int(input("Nivel de prioridad (1-5): "))
        SantiagoBLista.append((SantiagoBTarea, SantiagoBImportancia))
    SantiagoBLista.sort(key=lambda x: x[1], reverse=True)
    print("\nTareas ordenadas por prioridad:")
    for t in SantiagoBLista:
        print(f"{t[0]} (prioridad {t[1]})")

SantiagoBTareas()
