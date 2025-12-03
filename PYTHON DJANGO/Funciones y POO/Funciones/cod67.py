def SantiagoBPrestamo(SantiagoMonto, SantiagoInteres, SantiagoAnios):
    total = SantiagoMonto * (1 + SantiagoInteres / 100) ** SantiagoAnios
    return round(total, 2)

SantiagoMon = float(input("Monto del préstamo: "))
SantiagoInteres = float(input("Interés anual (%): "))
SantiagoEdad = int(input("Años: "))

print(f"Total a pagar: ${SantiagoBPrestamo(SantiagoMon, SantiagoInteres, SantiagoEdad)}")
