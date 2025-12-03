#Chateador simple según lo que responda el usuario

santiagoPreg = input("¿Cómo te sientes hoy? (bien/mal): ").lower()

if santiagoPreg == "bien":
    print("¡Me alegra! Ten un gran día")
elif santiagoPreg == "mal":
    print("Lo siento, espero que mejores pronto bro")
else:
    print("No entendí la respuesta repita el proceso")
