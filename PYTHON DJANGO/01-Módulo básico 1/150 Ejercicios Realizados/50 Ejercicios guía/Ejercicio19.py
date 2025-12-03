# Buscador en lista
santiagoEquips = ["nacional", "millonarios", "santa fe", "cali", "junior", "cali", "junior"]

print("Lista de equipos de futbol colombiano:", santiagoEquips)

# Buscar si un elemento existe
santiagoBusc = "cali"
if santiagoBusc in santiagoEquips: 
    print(f"\n {santiagoBusc} está en la lista")

    # Encontrar la primera posición
    santiagoPos = santiagoEquips.index(santiagoBusc) 
    print(f"Primera aparición en posición: {santiagoPos}")

    # Contar cuántas veces aparece
    santiagoCant = santiagoEquips.count(santiagoBusc) 
    print(f"Aparece {santiagoCant} veces en total")
else:
    print(f"\n {santiagoBusc} no está en la lista")

# Buscar múltiples elementos
santiagoBuscs = ["millonarios", "nacional", "cali"]
print(f"\nBuscando: {santiagoBuscs}")

for santiagoT in santiagoBuscs:
    if santiagoT in santiagoEquips:
        santiagoPos = santiagoEquips.index(santiagoT)
        print(f"{santiagoT} encontrado en posición {santiagoPos}")
    else:
        print(f"{santiagoT} no encontrado")