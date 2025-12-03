#Traductor de palabras

santiagoDic = {"casa": "house", "libro": "book", "perro": "dog"}

santiagoPal = input("Ingrese una palabra en español: ").lower()
print("Traducción:", santiagoDic.get(santiagoPal, "No encontrada"))
