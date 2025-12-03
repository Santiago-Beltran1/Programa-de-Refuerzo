#Sistema que imprime las palabra con más de cinco caracteres

santiagoPals = ["Arroz", "papa", "Lentejas", "piña", "Cebolla"]
santiagoLgs = [p for p in santiagoPals if len(p) > 5]
print("Palabras largas:", santiagoLgs)
