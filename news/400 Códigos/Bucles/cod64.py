SantiagoBCant = int(input("Ingrese cantidad de personas: "))
SantiagoMay = 0
SantiagoSum = 0

for SantiagoI in range(SantiagoBCant):
    SantiagoEdad = int(input("Edad de la persona: "))
    SantiagoSum += SantiagoEdad
    if SantiagoEdad >= 18:
        SantiagoMay += 1

SantiagoProm = SantiagoSum / SantiagoBCant
print(f"Promedio de edad: {SantiagoProm}")
print(f"Mayores de edad: {SantiagoMay}")
