#Analizador de edades y cuáles son mayores de edad

santiagoEdades = {"Ana": 20, "Luis": 17, "Juan": 25}
santiagoMayores = {k: v for k, v in santiagoEdades.items() if v >= 18}
print("Mayores de edad:", santiagoMayores)
